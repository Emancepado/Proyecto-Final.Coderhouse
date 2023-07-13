from django.urls import path
from . import views 

urlpatterns = [
    path('registration/', views.registration, name = 'registro'),
    path('', views.loginWeb, name='login' ),
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout_view, name = 'logout'),
    path('editarPerfil', views.editarPerfil, name='editarPerfil'),
    path('editarContraseña', views.editarContraseña, name='editarContraseña'),
    path('editarAvatar', views.editarAvatar, name='editarAvatar'),


]