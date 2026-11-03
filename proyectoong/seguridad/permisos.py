from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render

from .utils import registrar


def _denegar(request, requisito):
    registrar(request, 'ACCESO_DENEGADO',
              detalle=f'{request.method} {request.path} (requiere {requisito})')
    if not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())
    return render(request, '403.html', status=403)


def solo_superusuario(vista):
    @wraps(vista)
    def envoltura(request, *args, **kwargs):
        if not (request.user.is_active and request.user.is_superuser):
            return _denegar(request, 'administrador')
        return vista(request, *args, **kwargs)
    return envoltura


def solo_personal(vista):
    """Administradores y operadores (is_staff). Excluye cuentas registradas solas."""
    @wraps(vista)
    def envoltura(request, *args, **kwargs):
        if not (request.user.is_active and request.user.is_staff):
            return _denegar(request, 'personal')
        return vista(request, *args, **kwargs)
    return envoltura