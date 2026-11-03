from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from seguridad.models import Bitacora
from seguridad.utils import ROLES, aplicar_rol, dejaria_sin_admins, rol_de


class Command(BaseCommand):
    help = 'Cambia el rol de un usuario (admin/operador/registrado). Único modo de crear o quitar administradores.'

    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('rol', choices=['admin', 'operador', 'registrado'])

    def handle(self, *args, **opciones):
        try:
            user = User.objects.get(username=opciones['username'])
        except User.DoesNotExist:
            raise CommandError('No existe ese usuario')
        nuevo = {'admin': 'ADMIN', 'operador': 'OPERADOR', 'registrado': 'REGISTRADO'}[opciones['rol']]
        anterior = rol_de(user)
        if anterior == nuevo:
            raise CommandError('Ya tiene ese rol.')
        if anterior == 'ADMIN' and dejaria_sin_admins(user):
            raise CommandError('Es el último administrador activo: no se le puede quitar el rol.')
        aplicar_rol(user, nuevo)
        Bitacora.objects.create(
            usuario='CONSOLA', accion='ROL_CAMBIADO', tabla='auth_user',
            objeto_id=str(user.id),
            detalle=f'{user.username}: {ROLES[anterior]} -> {ROLES[nuevo]} (por consola)')
        self.stdout.write(self.style.SUCCESS(f'{user.username}: {ROLES[anterior]} -> {ROLES[nuevo]}'))