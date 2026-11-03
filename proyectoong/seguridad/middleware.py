import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import BloqueoUsuario
from .utils import registrar


class InactividadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # 1) ¿la cuenta fue bloqueada mientras tenía la sesión abierta?
            if BloqueoUsuario.objects.filter(usuario=request.user, bloqueado=True).exists():
                registrar(request, 'SESION_REVOCADA', detalle='Cuenta bloqueada con sesión activa')
                logout(request)
                messages.error(request, 'Su cuenta fue bloqueada. Contacte a un administrador.')
                return redirect('login')

            # 2) ¿pasó demasiado tiempo sin actividad?
            ahora = time.time()
            ultima = request.session.get('ultima_actividad')
            if ultima is not None and ahora - ultima > settings.TIEMPO_INACTIVIDAD:
                registrar(request, 'SESION_EXPIRADA',
                          detalle=f'Inactivo más de {settings.TIEMPO_INACTIVIDAD // 60} min')
                logout(request)
                messages.warning(request, 'Su sesión expiró por inactividad. Inicie sesión de nuevo.')
                return redirect('login')
            request.session['ultima_actividad'] = ahora
        return self.get_response(request)