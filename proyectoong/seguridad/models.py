from django.conf import settings
from django.db import models


class Bitacora(models.Model):
    usuario = models.CharField(max_length=150, blank=True)  # texto: también sirve para usuarios inexistentes
    accion = models.CharField(max_length=30)
    tabla = models.CharField(max_length=50, blank=True)
    objeto_id = models.CharField(max_length=50, blank=True)
    detalle = models.CharField(max_length=500, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']


class BloqueoUsuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    intentos_fallidos = models.PositiveIntegerField(default=0)
    bloqueado = models.BooleanField(default=False)
    fecha_bloqueo = models.DateTimeField(null=True, blank=True)