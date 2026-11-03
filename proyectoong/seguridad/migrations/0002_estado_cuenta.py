from django.db import migrations, models


def bloqueado_a_estado(apps, schema_editor):
    BloqueoUsuario = apps.get_model('seguridad', 'BloqueoUsuario')
    for b in BloqueoUsuario.objects.filter(bloqueado=True):
        b.estado = 'SUSPENDIDA'
        b.motivo = 'Superó el máximo de intentos de contraseña'
        b.cambiado_por = 'SISTEMA'
        b.fecha_estado = b.fecha_bloqueo
        b.save()


def estado_a_bloqueado(apps, schema_editor):
    BloqueoUsuario = apps.get_model('seguridad', 'BloqueoUsuario')
    for b in BloqueoUsuario.objects.filter(estado='SUSPENDIDA'):
        b.bloqueado = True
        b.fecha_bloqueo = b.fecha_estado
        b.save()


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.AddField('bloqueousuario', 'estado',
            models.CharField(choices=[('ACTIVA', 'Activa'), ('SUSPENDIDA', 'Suspendida')],
                             default='ACTIVA', max_length=12)),
        migrations.AddField('bloqueousuario', 'motivo',
            models.CharField(blank=True, max_length=200)),
        migrations.AddField('bloqueousuario', 'cambiado_por',
            models.CharField(blank=True, max_length=150)),
        migrations.AddField('bloqueousuario', 'fecha_estado',
            models.DateTimeField(blank=True, null=True)),
        migrations.RunPython(bloqueado_a_estado, estado_a_bloqueado),
        migrations.RemoveField('bloqueousuario', 'bloqueado'),
        migrations.RemoveField('bloqueousuario', 'fecha_bloqueo'),
    ]