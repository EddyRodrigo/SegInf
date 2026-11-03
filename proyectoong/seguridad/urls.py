from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/<int:id>/suspender/', views.suspender_usuario, name='suspender_usuario'),
    path('usuarios/<int:id>/activar/', views.activar_usuario, name='activar_usuario'),
    path('usuarios/<int:id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('log/', views.ver_log, name='ver_log'),
]