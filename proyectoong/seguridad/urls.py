from django.urls import path
from . import views

urlpatterns = [
    path('bloqueados/', views.usuarios_bloqueados, name='usuarios_bloqueados'),
    path('habilitar/<int:id>/', views.habilitar_usuario, name='habilitar_usuario'),
    path('log/', views.ver_log, name='ver_log'),
]