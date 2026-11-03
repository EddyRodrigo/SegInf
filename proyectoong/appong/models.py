# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    evento = models.ForeignKey('Evento', models.DO_NOTHING, db_column='id_evento')
    voluntario = models.ForeignKey('Voluntario', models.DO_NOTHING, db_column='id_voluntario')
    hora_llegada = models.DateTimeField()
    hora_salida = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencias'

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    proposito = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eventos'

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    evento = models.ForeignKey('Evento', models.DO_NOTHING, db_column='id_evento')
    voluntario = models.ForeignKey('Voluntario', models.DO_NOTHING, db_column='id_voluntario')
    rol = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'inscripciones'

class Voluntario(models.Model):
    id_voluntario = models.AutoField(primary_key=True)
    ci = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=255, unique=True)
    telefono = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'voluntarios'

    def __str__(self):
        return self.nombre+" "+self.apellido