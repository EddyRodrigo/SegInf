from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from seguridad.views import LoginSeguro

urlpatterns = [
    path("", views.index, name = "index"),
    path("hello/", views.index, name = "principal"),
    # path("login/", auth_views.LoginView.as_view(template_name = "Front_end/login.html"), name = "login"),
    path("login/", LoginSeguro.as_view(), name="login"),
    path("logout/", views.cerrar_sesion, name = "logout"),
    path("registro/", views.registro, name = "registro"),
    path("verificar/<str:token>/", views.verificar_correo, name="verificar_correo"),
]