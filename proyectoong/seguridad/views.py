from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Bitacora, BloqueoUsuario
from .permisos import solo_superusuario as solo_admin
from .utils import cambiar_estado, estado_de, registrar

MENSAJE_GENERICO = 'Usuario o contraseña incorrectos, o la cuenta no está disponible.'
MOTIVO_INTENTOS = 'Superó el máximo de intentos de contraseña'


class LoginSeguro(LoginView):
    template_name = 'Front_end/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '').strip()
        if BloqueoUsuario.objects.filter(usuario__username=username,
                                         estado=BloqueoUsuario.SUSPENDIDA).exists():
            registrar(request, 'LOGIN_RECHAZADO', usuario=username, detalle='Cuenta suspendida')
            form = self.get_form()
            form.add_error(None, MENSAJE_GENERICO)
            return self.render_to_response(self.get_context_data(form=form))
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        BloqueoUsuario.objects.filter(usuario=user).update(intentos_fallidos=0)
        response = super().form_valid(form)  # aquí ya se inicia la sesión
        registrar(self.request, 'LOGIN_OK', usuario=user.username)
        return response

    def form_invalid(self, form):
        username = self.request.POST.get('username', '').strip()
        user = User.objects.filter(username=username).first()
        if user:
            with transaction.atomic():
                b, _ = BloqueoUsuario.objects.select_for_update().get_or_create(usuario=user)
                b.intentos_fallidos += 1
                recien_suspendida = (b.intentos_fallidos >= settings.MAX_INTENTOS_LOGIN
                                     and b.estado == BloqueoUsuario.ACTIVA)
                if recien_suspendida:
                    b.estado = BloqueoUsuario.SUSPENDIDA
                    b.motivo = MOTIVO_INTENTOS
                    b.cambiado_por = 'SISTEMA'
                    b.fecha_estado = timezone.now()
                b.save()
            registrar(self.request, 'LOGIN_FALLIDO', usuario=username,
                      detalle=f'Intento {b.intentos_fallidos} de {settings.MAX_INTENTOS_LOGIN}')
            if recien_suspendida:
                registrar(self.request, 'ESTADO_CAMBIADO', usuario='SISTEMA',
                          tabla='auth_user', objeto_id=user.id,
                          detalle=f'{username}: ACTIVA -> SUSPENDIDA. Motivo: {MOTIVO_INTENTOS}')
        else:
            registrar(self.request, 'LOGIN_FALLIDO', usuario=username, detalle='Usuario inexistente')
        return super().form_invalid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.error_messages = {
            **form.error_messages,
            'invalid_login': MENSAJE_GENERICO,
            'inactive': MENSAJE_GENERICO,
        }
        return form


# ---------- Gestión de usuarios ----------

@solo_admin
def usuarios(request):
    filtro = request.GET.get('estado', '').strip().upper()
    filas = []
    for u in User.objects.select_related('bloqueousuario').order_by('username'):
        b = getattr(u, 'bloqueousuario', None)   # sin fila = activa
        estado = b.estado if b else BloqueoUsuario.ACTIVA
        es_yo = u.pk == request.user.pk
        filas.append({
            'usuario': u,
            'rol': 'Administrador' if u.is_superuser else ('Operador' if u.is_staff else 'Registrado'),
            'estado': estado,
            'estado_texto': 'Activa' if estado == BloqueoUsuario.ACTIVA else 'Suspendida',
            'motivo': b.motivo if b else '',
            'cambiado_por': b.cambiado_por if b else '',
            'fecha_estado': b.fecha_estado if b else None,
            'es_yo': es_yo,
            'puede_eliminar': not es_yo and not u.is_superuser,   # admins: solo por consola
        })
    n_activas = sum(1 for f in filas if f['estado'] == BloqueoUsuario.ACTIVA)
    n_suspendidas = len(filas) - n_activas
    if filtro in (BloqueoUsuario.ACTIVA, BloqueoUsuario.SUSPENDIDA):
        filas = [f for f in filas if f['estado'] == filtro]
    # suspendidas primero (ahí caen las pendientes de activación)
    filas.sort(key=lambda f: (f['estado'] == BloqueoUsuario.ACTIVA, f['usuario'].username.lower()))
    return render(request, 'seguridad/usuarios.html', {
        'filas': filas, 'filtro': filtro,
        'n_total': n_activas + n_suspendidas,
        'n_activas': n_activas, 'n_suspendidas': n_suspendidas,
    })


def _aplicar_estado(request, objetivo, nuevo, motivo):
    if objetivo.pk == request.user.pk:
        registrar(request, 'ACCESO_DENEGADO', tabla='auth_user', objeto_id=objetivo.id,
                  detalle='Intentó cambiar su propio estado')
        messages.error(request, 'No puede cambiar el estado de su propia cuenta.')
        return redirect('usuarios')
    if estado_de(objetivo) == nuevo:
        messages.info(request, f'{objetivo.username} ya estaba en ese estado.')
        return redirect('usuarios')
    anterior = cambiar_estado(objetivo, nuevo, motivo, request.user.username)
    registrar(request, 'ESTADO_CAMBIADO', tabla='auth_user', objeto_id=objetivo.id,
              detalle=f'{objetivo.username}: {anterior} -> {nuevo}. Motivo: {motivo}')
    messages.success(request, f'{objetivo.username}: {anterior} → {nuevo}.')
    return redirect('usuarios')


@solo_admin
@require_POST
def suspender_usuario(request, id):
    objetivo = get_object_or_404(User, pk=id)
    motivo = request.POST.get('motivo', '').strip()[:150] or 'Decisión de un administrador'
    return _aplicar_estado(request, objetivo, BloqueoUsuario.SUSPENDIDA, motivo)


@solo_admin
@require_POST
def activar_usuario(request, id):
    objetivo = get_object_or_404(User, pk=id)
    return _aplicar_estado(request, objetivo, BloqueoUsuario.ACTIVA, 'Activada por un administrador')


@solo_admin
@require_POST
def eliminar_usuario(request, id):
    objetivo = get_object_or_404(User, pk=id)
    if objetivo.pk == request.user.pk:
        registrar(request, 'ACCESO_DENEGADO', tabla='auth_user', objeto_id=id,
                  detalle='Intentó eliminar su propia cuenta')
        messages.error(request, 'No puede eliminar su propia cuenta.')
        return redirect('usuarios')
    if objetivo.is_superuser:
        registrar(request, 'ACCESO_DENEGADO', tabla='auth_user', objeto_id=id,
                  detalle=f'Intentó eliminar al administrador {objetivo.username} desde la web')
        messages.error(request, 'Los administradores solo pueden eliminarse por consola.')
        return redirect('usuarios')
    nombre = objetivo.username
    rol = 'operador' if objetivo.is_staff else 'registrado'
    registrar(request, 'USUARIO_ELIMINADO', tabla='auth_user', objeto_id=id,
              detalle=f'Eliminó a {nombre} ({rol})')
    objetivo.delete()   # BloqueoUsuario se borra en cascada; la bitácora conserva el historial
    messages.success(request, f'Usuario {nombre} eliminado.')
    return redirect('usuarios')


@solo_admin
def ver_log(request):
    registros = Bitacora.objects.all()
    usuario = request.GET.get('usuario', '').strip()
    accion = request.GET.get('accion', '').strip()
    if usuario:
        registros = registros.filter(usuario__icontains=usuario)
    if accion:
        registros = registros.filter(accion=accion)
    acciones = Bitacora.objects.order_by().values_list('accion', flat=True).distinct()
    return render(request, 'seguridad/log.html', {
        'registros': registros[:200], 'acciones': acciones,
        'usuario': usuario, 'accion_sel': accion,
    })