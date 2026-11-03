from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from .permisos import solo_superusuario as solo_admin

from .models import Bitacora, BloqueoUsuario
from .utils import registrar
from django.db import transaction

MENSAJE_GENERICO = 'Usuario o contraseña incorrectos, o la cuenta no está disponible.'



class LoginSeguro(LoginView):
    template_name = 'Front_end/login.html'

    

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '').strip()
        bloqueo = BloqueoUsuario.objects.filter(usuario__username=username, bloqueado=True).first()
        if bloqueo:
            registrar(request, 'LOGIN_RECHAZADO', usuario=username, detalle='Cuenta bloqueada')
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
                recien_bloqueada = (b.intentos_fallidos >= settings.MAX_INTENTOS_LOGIN
                                    and not b.bloqueado)
                if recien_bloqueada:
                    b.bloqueado = True
                    b.fecha_bloqueo = timezone.now()
                b.save()
            registrar(self.request, 'LOGIN_FALLIDO', usuario=username,
                      detalle=f'Intento {b.intentos_fallidos} de {settings.MAX_INTENTOS_LOGIN}')
            if recien_bloqueada:
                registrar(self.request, 'CUENTA_BLOQUEADA', usuario=username,
                          detalle='Superó el máximo de intentos')
        else:
            registrar(self.request, 'LOGIN_FALLIDO', usuario=username, detalle='Usuario inexistente')
        return super().form_invalid(form)

#si falla trata de quitar esto jejeje
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.error_messages = {
            **form.error_messages,
            'invalid_login': MENSAJE_GENERICO,
            'inactive': MENSAJE_GENERICO,
        }
        return form

    


@solo_admin
def usuarios_bloqueados(request):
    bloqueos = BloqueoUsuario.objects.filter(bloqueado=True).select_related('usuario')
    return render(request, 'seguridad/usuarios_bloqueados.html', {'bloqueos': bloqueos})


@solo_admin
@require_POST
def habilitar_usuario(request, id):
    b = get_object_or_404(BloqueoUsuario, usuario_id=id)
    b.bloqueado = False
    b.intentos_fallidos = 0
    b.fecha_bloqueo = None
    b.save()
    registrar(request, 'USUARIO_HABILITADO', tabla='auth_user', objeto_id=id,
              detalle=f'Habilitó a {b.usuario.username}')
    return redirect('usuarios_bloqueados')


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