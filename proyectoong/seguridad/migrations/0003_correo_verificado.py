from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0002_estado_cuenta'),
    ]

    operations = [
        migrations.AddField('bloqueousuario', 'correo_verificado',
                            models.BooleanField(default=True)),
    ]