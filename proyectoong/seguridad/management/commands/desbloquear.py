from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from seguridad.models import Bitacora, BloqueoUsuario


class Command(BaseCommand):
    help = 'Desbloquea una cuenta desde la consola (procedimiento de emergencia)'

    def add_arguments(self, parser):
        parser.add_argument('username')

    def handle(self, *args, **opciones):
        try:
            user = User.objects.get(username=opciones['username'])
        except User.DoesNotExist:
            raise CommandError('No existe ese usuario')
        BloqueoUsuario.objects.filter(usuario=user).update(
            bloqueado=False, intentos_fallidos=0, fecha_bloqueo=None)
        Bitacora.objects.create(
            usuario='CONSOLA', accion='DESBLOQUEO_EMERGENCIA', tabla='auth_user',
            objeto_id=str(user.id), detalle=f'Desbloqueó a {user.username} por consola')
        self.stdout.write(self.style.SUCCESS(f'{user.username} desbloqueado.'))