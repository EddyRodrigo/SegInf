from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Voluntario, Inscripcion, Asistencia
from .forms import EventoForm, VoluntarioForm, InscripcionForm, AsistenciaForm
from seguridad.utils import registrar


def intro(request):
    return render(request, 'appong/intro.html')


# CRUD Eventos
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'appong/Eventos/lista_eventos.html', {'eventos': eventos})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            registrar(request, 'CREAR', tabla='eventos',
                      objeto_id=evento.id_evento, detalle=evento.nombre)
            return redirect('eventos')
    else:
        form = EventoForm()
    return render(request, 'appong/Eventos/nuevo_evento.html', {'form': form})


def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id_evento=id)
    registrar(request, 'ELIMINAR', tabla='eventos',
              objeto_id=id, detalle=evento.nombre)
    evento.delete()
    return redirect('eventos')


def modificar_evento(request, id):
    evento = get_object_or_404(Evento, id_evento=id)
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento.nombre = form.cleaned_data['nombre']
            evento.proposito = form.cleaned_data['proposito']
            evento.fecha_inicio = form.cleaned_data['fecha_inicio']
            evento.fecha_fin = form.cleaned_data['fecha_fin']
            evento.save()
            registrar(request, 'MODIFICAR', tabla='eventos',
                      objeto_id=id, detalle=evento.nombre)
            return redirect('eventos')
    else:
        form = EventoForm(initial={
            'nombre': evento.nombre,
            'proposito': evento.proposito,
            'fecha_inicio': evento.fecha_inicio,
            'fecha_fin': evento.fecha_fin,
        })
    return render(request, 'appong/Eventos/actualizar_evento.html', {'form': form})


# CRUD Voluntarios
def listar_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'appong/Voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})


def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            voluntario = form.save()
            registrar(request, 'CREAR', tabla='voluntarios',
                      objeto_id=voluntario.id_voluntario,
                      detalle=f'{voluntario.nombre} {voluntario.apellido}')
            return redirect('voluntarios')
    else:
        form = VoluntarioForm()
    return render(request, 'appong/Voluntarios/nuevo_voluntario.html', {'form': form})


def eliminar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    registrar(request, 'ELIMINAR', tabla='voluntarios', objeto_id=id,
              detalle=f'{voluntario.nombre} {voluntario.apellido}')
    voluntario.delete()
    return redirect('voluntarios')


def modificar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            voluntario.ci = int(form.cleaned_data['ci'])
            voluntario.nombre = form.cleaned_data['nombre']
            voluntario.apellido = form.cleaned_data['apellido']
            voluntario.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            voluntario.correo = form.cleaned_data['correo']
            voluntario.telefono = int(form.cleaned_data['telefono'])
            voluntario.save()
            registrar(request, 'MODIFICAR', tabla='voluntarios', objeto_id=id,
                      detalle=f'{voluntario.nombre} {voluntario.apellido}')
            return redirect('voluntarios')
    else:
        form = VoluntarioForm(initial={
            'ci': voluntario.ci,
            'nombre': voluntario.nombre,
            'apellido': voluntario.apellido,
            'fecha_nacimiento': voluntario.fecha_nacimiento,
            'correo': voluntario.correo,
            'telefono': voluntario.telefono,
        })
    return render(request, 'appong/Voluntarios/actualizar_voluntario.html', {'form': form})


# CRUD Inscripciones
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'appong/Inscripciones/lista_inscripciones.html', {'inscripciones': inscripciones})


def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save()
            registrar(request, 'CREAR', tabla='inscripciones',
                      objeto_id=inscripcion.id_inscripcion,
                      detalle=f'evento {inscripcion.evento_id}, voluntario {inscripcion.voluntario_id}, rol {inscripcion.rol}')
            return redirect('inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'appong/Inscripciones/nueva_inscripcion.html', {'form': form})


def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id_inscripcion=id)
    registrar(request, 'ELIMINAR', tabla='inscripciones', objeto_id=id,
              detalle=f'evento {inscripcion.evento_id}, voluntario {inscripcion.voluntario_id}')
    inscripcion.delete()
    return redirect('inscripciones')


def modificar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id_inscripcion=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion.evento = form.cleaned_data['evento']
            inscripcion.voluntario = form.cleaned_data['voluntario']
            inscripcion.rol = form.cleaned_data['rol']
            inscripcion.save()
            registrar(request, 'MODIFICAR', tabla='inscripciones', objeto_id=id,
                      detalle=f'evento {inscripcion.evento_id}, voluntario {inscripcion.voluntario_id}, rol {inscripcion.rol}')
            return redirect('inscripciones')
    else:
        form = InscripcionForm(initial={
            'evento': inscripcion.evento,
            'voluntario': inscripcion.voluntario,
            'rol': inscripcion.rol,
        })
    return render(request, 'appong/Inscripciones/actualizar_inscripcion.html', {'form': form})


# CRUD Asistencias
def listar_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'appong/Asistencias/lista_asistencias.html', {'asistencias': asistencias})


def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()
            registrar(request, 'CREAR', tabla='asistencias',
                      objeto_id=asistencia.id_asistencia,
                      detalle=f'evento {asistencia.evento_id}, voluntario {asistencia.voluntario_id}')
            return redirect('asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'appong/Asistencias/nueva_asistencia.html', {'form': form})


def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id_asistencia=id)
    registrar(request, 'ELIMINAR', tabla='asistencias', objeto_id=id,
              detalle=f'evento {asistencia.evento_id}, voluntario {asistencia.voluntario_id}')
    asistencia.delete()
    return redirect('asistencias')


def modificar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id_asistencia=id)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia.evento = form.cleaned_data['evento']
            asistencia.voluntario = form.cleaned_data['voluntario']
            asistencia.hora_llegada = form.cleaned_data['hora_llegada']
            asistencia.hora_salida = form.cleaned_data['hora_salida']
            asistencia.save()
            registrar(request, 'MODIFICAR', tabla='asistencias', objeto_id=id,
                      detalle=f'evento {asistencia.evento_id}, voluntario {asistencia.voluntario_id}')
            return redirect('asistencias')
    else:
        form = AsistenciaForm(initial={
            'evento': asistencia.evento,
            'voluntario': asistencia.voluntario,
            'hora_llegada': asistencia.hora_llegada,
            'hora_salida': asistencia.hora_salida,
        })
    return render(request, 'appong/Asistencias/actualizar_asistencia.html', {'form': form})


# Funcionalidad Voluntarios
def horas_acumuladas(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    asistencias = Asistencia.objects.filter(voluntario=voluntario)
    total_minutos = 0

    for asistencia in asistencias:
        salida = asistencia.hora_salida
        llegada = asistencia.hora_llegada
        total_minutos += (salida.hour - llegada.hour) * 60 + (salida.minute - llegada.minute)

    horas = total_minutos // 60
    minutos = total_minutos % 60

    return render(request, 'appong/Funcionalidades/horas_acumuladas.html',
                  {'voluntario': voluntario, 'horas': horas, 'minutos': minutos})


# Cambiar Rol
def cambiar_rol(request, id):
    inscripcion = get_object_or_404(Inscripcion, id_inscripcion=id)
    if request.method == 'POST':
        rol_anterior = inscripcion.rol
        inscripcion.rol = request.POST.get('rol')
        inscripcion.save()
        registrar(request, 'MODIFICAR', tabla='inscripciones', objeto_id=id,
                  detalle=f'Rol: {rol_anterior} -> {inscripcion.rol}')
        return redirect('inscripciones')

    return render(request, 'appong/Funcionalidades/cambiarRol.html', {'inscripcion': inscripcion})


def hoja_asistencia_evento(request, id):
    evento = get_object_or_404(Evento, id_evento=id)
    asistencias = Asistencia.objects.filter(evento=evento)
    return render(request, 'appong/Funcionalidades/hoja_asistencia.html',
                  {'asistencias': asistencias, 'evento': evento})


def eventos_participados(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    inscripciones = Inscripcion.objects.filter(voluntario=voluntario)
    return render(request, 'appong/Funcionalidades/eventos_participados.html',
                  {'inscripciones': inscripciones, 'voluntario': voluntario})