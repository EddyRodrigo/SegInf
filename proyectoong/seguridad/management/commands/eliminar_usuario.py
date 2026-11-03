from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from seguridad.models import Bitacora
from seguridad.utils import dejaria_sin_admins


class Command(BaseCommand):
    help = 'Elimina un usuario (único modo de eliminar administradores).'

    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('--yes', action='store_true', help='No pedir confirmación')

    def handle(self, *args, **opciones):
        try:
            user = User.objects.get(username=opciones['username'])
        except User.DoesNotExist:
            raise CommandError('No existe ese usuario')
        if dejaria_sin_admins(user):
            raise CommandError('Es el último administrador activo: no se puede eliminar.')
        if not opciones['yes']:
            if input(f'Escriba "{user.username}" para confirmar la eliminación: ') != user.username:
                raise CommandError('Cancelado.')
        rol = 'administrador' if user.is_superuser else ('operador' if user.is_staff else 'registrado')
        Bitacora.objects.create(
            usuario='CONSOLA', accion='USUARIO_ELIMINADO', tabla='auth_user',
            objeto_id=str(user.id), detalle=f'Eliminó a {user.username} ({rol}) por consola')
        user.delete()
        self.stdout.write(self.style.SUCCESS(f'{opciones["username"]} eliminado.'))