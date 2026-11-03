from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from seguridad.models import Bitacora, BloqueoUsuario
from seguridad.utils import cambiar_estado, dejaria_sin_admins


class Command(BaseCommand):
    help = 'Cambia el estado de una cuenta (activa/suspendida) desde la consola. Uso de emergencia.'

    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('estado', choices=['activa', 'suspendida'])
        parser.add_argument('--motivo', default='Cambio por consola')

    def handle(self, *args, **opciones):
        try:
            user = User.objects.get(username=opciones['username'])
        except User.DoesNotExist:
            raise CommandError('No existe ese usuario')
        nuevo = BloqueoUsuario.ACTIVA if opciones['estado'] == 'activa' else BloqueoUsuario.SUSPENDIDA
        if nuevo == BloqueoUsuario.SUSPENDIDA and dejaria_sin_admins(user):
            raise CommandError('Es el último administrador activo: no se puede suspender.')
        anterior = cambiar_estado(user, nuevo, opciones['motivo'], 'CONSOLA')
        Bitacora.objects.create(
            usuario='CONSOLA', accion='ESTADO_EMERGENCIA', tabla='auth_user',
            objeto_id=str(user.id),
            detalle=f'{user.username}: {anterior} -> {nuevo}. Motivo: {opciones["motivo"]}'[:500])
        self.stdout.write(self.style.SUCCESS(f'{user.username}: {anterior} -> {nuevo}'))