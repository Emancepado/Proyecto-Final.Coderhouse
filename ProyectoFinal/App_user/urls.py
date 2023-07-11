from django.urls import path
from . import views 

urlpatterns = [
    path('registration/', views.registration, name = 'registro'),
    path('', views.loginWeb, name='login' ),
    path('home/', views.home, name = 'home')


]