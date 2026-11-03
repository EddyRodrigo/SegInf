from django.contrib.auth.models import User
from django.utils import timezone

from .models import Bitacora, BloqueoUsuario


def registrar(request, accion, usuario=None, tabla='', objeto_id='', detalle=''):
    if usuario is None:
        usuario = request.user.username if request.user.is_authenticated else ''
    Bitacora.objects.create(
        usuario=usuario,
        accion=accion,
        tabla=tabla,
        objeto_id=str(objeto_id),
        detalle=detalle[:500],
        ip=request.META.get('REMOTE_ADDR'),
    )


def estado_de(user):
    """Sin fila en BloqueoUsuario = cuenta activa."""
    b = BloqueoUsuario.objects.filter(usuario=user).first()
    return b.estado if b else BloqueoUsuario.ACTIVA


def cambiar_estado(usuario, nuevo, motivo, por):
    """Cambia el estado y devuelve el anterior. El registro en bitácora lo hace quien llama."""
    b, _ = BloqueoUsuario.objects.get_or_create(usuario=usuario)
    anterior = b.estado
    b.estado = nuevo
    b.motivo = motivo[:200]
    b.cambiado_por = por
    b.fecha_estado = timezone.now()
    if nuevo == BloqueoUsuario.ACTIVA:
        b.intentos_fallidos = 0
    b.save()
    return anterior


def dejaria_sin_admins(user):
    """True si suspender o eliminar a este usuario dejaría al sistema sin ningún admin activo."""
    if not user.is_superuser:
        return False
    otros = (User.objects.filter(is_superuser=True, is_active=True)
             .exclude(pk=user.pk)
             .exclude(bloqueousuario__estado=BloqueoUsuario.SUSPENDIDA))
    return not otros.exists()