from .models import Bitacora


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