import smtplib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core import signing
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse

from seguridad.models import BloqueoUsuario
from seguridad.utils import registrar, cambiar_estado

from .forms import RegistroForm

SAL_VERIFICACION = 'verificar-correo'


def index(request):
    if request.user.is_authenticated:
        return render(request, 'Front_end/index.html')
    else:
        return redirect('login')


def cerrar_sesion(request):
    registrar(request, 'LOGOUT')
    logout(request)
    return redirect('index')


def _enviar_verificacion(request, usuario):
    """Envía el enlace firmado. Si el correo falla, lanza la excepción a quien llama."""
    token = signing.dumps({'uid': usuario.pk, 'email': usuario.email}, salt=SAL_VERIFICACION)
    enlace = request.build_absolute_uri(reverse('verificar_correo', args=[token]))
    horas = getattr(settings, 'VERIFICACION_MAX_EDAD', 24 * 3600) // 3600
    send_mail(
        'Verifique su correo - ONG',
        f'Hola {usuario.username},\n\n'
        f'Para verificar su correo abra este enlace (vale {horas} horas):\n{enlace}\n\n'
        'Si usted no creó esta cuenta, ignore este mensaje.',
        settings.DEFAULT_FROM_EMAIL,
        [usuario.email],
        fail_silently=False,
    )


# Crear cuenta
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():   # si el correo falla, la cuenta no se crea
                    usuario = form.save(commit=False)
                    usuario.is_superuser = False
                    usuario.is_staff = False
                    usuario.save()
                    cambiar_estado(usuario, BloqueoUsuario.SUSPENDIDA,
                                   'Pendiente de activación', 'SISTEMA')
                    BloqueoUsuario.objects.filter(usuario=usuario).update(correo_verificado=False)
                    _enviar_verificacion(request, usuario)
            except (smtplib.SMTPException, OSError):
                registrar(request, 'CORREO_ERROR', usuario=form.cleaned_data['username'],
                          detalle='No se pudo enviar el correo de verificación; registro cancelado')
                messages.error(request, 'No se pudo enviar el correo de verificación. Intente más tarde.')
                return render(request, 'Front_end/registro.html', {'form': form})
            registrar(request, 'USUARIO_REGISTRADO', usuario=usuario.username,
                      tabla='auth_user', objeto_id=usuario.id,
                      detalle='Cuenta creada desde /registro/, estado SUSPENDIDA (pendiente de verificación y activación)')
            messages.info(request, 'Cuenta creada. Abra el enlace que le enviamos por correo; '
                                   'después un administrador debe activarla antes de que pueda ingresar.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'Front_end/registro.html', {'form': form})


def verificar_correo(request, token):
    max_edad = getattr(settings, 'VERIFICACION_MAX_EDAD', 24 * 3600)
    try:
        datos = signing.loads(token, salt=SAL_VERIFICACION, max_age=max_edad)
    except signing.BadSignature:   # incluye enlace alterado y enlace vencido
        registrar(request, 'VERIFICACION_INVALIDA', detalle='Enlace alterado o vencido')
        messages.error(request, 'El enlace no es válido o venció.')
        return redirect('login')

    usuario = User.objects.filter(pk=datos.get('uid'), email=datos.get('email')).first()
    if usuario is None:
        registrar(request, 'VERIFICACION_INVALIDA', detalle='El usuario del enlace ya no existe o cambió de correo')
        messages.error(request, 'El enlace no es válido o venció.')
        return redirect('login')

    bloqueo = BloqueoUsuario.objects.filter(usuario=usuario).first()
    if bloqueo is None or bloqueo.correo_verificado:
        messages.info(request, 'Este correo ya estaba verificado.')
        return redirect('login')

    bloqueo.correo_verificado = True
    bloqueo.save(update_fields=['correo_verificado'])
    registrar(request, 'CORREO_VERIFICADO', usuario=usuario.username,
              tabla='auth_user', objeto_id=usuario.id, detalle='Correo verificado por enlace')
    messages.success(request, 'Correo verificado. Un administrador debe activar su cuenta para que pueda ingresar.')
    return redirect('login')


def error_404_view(request, exception):
    return render(request, '404.html', status=404)