from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from seguridad.utils import registrar   #*<------ esto mas
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
def registro (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit = False)
            usuario.is_superuser = False
            usuario.is_staff = False
            usuario.save()
            login(request,usuario)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'Front_end/registro.html', {'form': form})