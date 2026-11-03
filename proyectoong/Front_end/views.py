from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from seguridad.utils import registrar   #*<------ esto mas

from django.contrib import messages
from seguridad.models import BloqueoUsuario
from seguridad.utils import registrar, cambiar_estado
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'Front_end/index.html')
    else:
        return redirect('login')

#Cerrar Sesión Cuenta               <<<----------ORIGINAL
#def cerrar_sesion(request):
 #   logout(request)
  #  return redirect('index')
def cerrar_sesion(request):
    registrar(request, 'LOGOUT')
    logout(request)
    return redirect('index')


#Crear cuenta
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_superuser = False
            usuario.is_staff = False
            usuario.save()
            cambiar_estado(usuario, BloqueoUsuario.SUSPENDIDA,
                           'Pendiente de activación', 'SISTEMA')
            registrar(request, 'USUARIO_REGISTRADO', usuario=usuario.username,
                      tabla='auth_user', objeto_id=usuario.id,
                      detalle='Cuenta creada desde /registro/, estado SUSPENDIDA (pendiente de activación)')
            messages.info(request, 'Cuenta creada. Un administrador debe activarla antes de que pueda ingresar.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Front_end/registro.html', {'form': form})

def error_404_view(request, exception):
    return render(request, '404.html', status=404)