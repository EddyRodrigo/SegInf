from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Voluntario, Inscripcion, Asistencia
from .forms import EventoForm, VoluntarioForm, InscripcionForm, AsistenciaForm
from seguridad.utils import registrar
from django.contrib.auth.decorators import login_required
from seguridad.permisos import solo_superusuario
from seguridad.permisos import solo_personal
from datetime import timedelta

@login_required
def intro(request):
    return render(request, 'appong/intro.html')


# CRUD Eventos
@solo_personal
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'appong/Eventos/lista_eventos.html', {'eventos': eventos})

@solo_superusuario
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


@solo_superusuario
def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id_evento=id)
    registrar(request, 'ELIMINAR', tabla='eventos',
              objeto_id=id, detalle=evento.nombre)
    evento.delete()
    return redirect('eventos')

@solo_superusuario
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
@solo_personal
def listar_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'appong/Voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})

@solo_superusuario
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

@solo_superusuario
def eliminar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    registrar(request, 'ELIMINAR', tabla='voluntarios', objeto_id=id,
              detalle=f'{voluntario.nombre} {voluntario.apellido}')
    voluntario.delete()
    return redirect('voluntarios')

@solo_superusuario
def modificar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            registrar(request, 'MODIFICAR', tabla='voluntarios', objeto_id=id,
                      detalle=f'{voluntario.nombre} {voluntario.apellido}')
            return redirect('voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'appong/Voluntarios/actualizar_voluntario.html', {'form': form})


# CRUD Inscripciones
@solo_personal
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'appong/Inscripciones/lista_inscripciones.html', {'inscripciones': inscripciones})


@solo_superusuario
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


@solo_superusuario
def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id_inscripcion=id)
    registrar(request, 'ELIMINAR', tabla='inscripciones', objeto_id=id,
              detalle=f'evento {inscripcion.evento_id}, voluntario {inscripcion.voluntario_id}')
    inscripcion.delete()
    return redirect('inscripciones')


@solo_superusuario
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
@solo_personal
def listar_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'appong/Asistencias/lista_asistencias.html', {'asistencias': asistencias})


@solo_superusuario
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


@solo_superusuario
def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id_asistencia=id)
    registrar(request, 'ELIMINAR', tabla='asistencias', objeto_id=id,
              detalle=f'evento {asistencia.evento_id}, voluntario {asistencia.voluntario_id}')
    asistencia.delete()
    return redirect('asistencias')


@solo_superusuario
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
@solo_superusuario
def horas_acumuladas(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    asistencias = Asistencia.objects.filter(voluntario=voluntario)
    total = timedelta()
    for a in asistencias:
        if a.hora_salida and a.hora_salida > a.hora_llegada:
            total += a.hora_salida - a.hora_llegada
    horas, minutos = divmod(int(total.total_seconds()) // 60, 60)
    return render(request, 'appong/Funcionalidades/horas_acumuladas.html',
                  {'voluntario': voluntario, 'horas': horas, 'minutos': minutos})


# Cambiar Rol
@solo_superusuario
def cambiar_rol(request, id):
    inscripcion = get_object_or_404(Inscripcion, id_inscripcion=id)
    if request.method == 'POST':
        rol = request.POST.get('rol', '').strip()
        if not rol or len(rol) > 100:
            return render(request, 'appong/Funcionalidades/cambiarRol.html', {
                'inscripcion': inscripcion,
                'error': 'El rol debe tener entre 1 y 100 caracteres.'})
        rol_anterior = inscripcion.rol
        inscripcion.rol = rol
        inscripcion.save()
        registrar(request, 'MODIFICAR', tabla='inscripciones', objeto_id=id,
                  detalle=f'Rol: {rol_anterior} -> {inscripcion.rol}')
        return redirect('inscripciones')

    return render(request, 'appong/Funcionalidades/cambiarRol.html', {'inscripcion': inscripcion})


@solo_superusuario
def hoja_asistencia_evento(request, id):
    evento = get_object_or_404(Evento, id_evento=id)
    asistencias = Asistencia.objects.filter(evento=evento)
    return render(request, 'appong/Funcionalidades/hoja_asistencia.html',
                  {'asistencias': asistencias, 'evento': evento})


@solo_superusuario
def eventos_participados(request, id):
    voluntario = get_object_or_404(Voluntario, id_voluntario=id)
    inscripciones = Inscripcion.objects.filter(voluntario=voluntario)
    return render(request, 'appong/Funcionalidades/eventos_participados.html',
                  {'inscripciones': inscripciones, 'voluntario': voluntario})