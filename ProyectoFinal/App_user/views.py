from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'El email ya está registrado.')
            else:
                form.save()
                return redirect('../')
    
    else: 
        form = RegistroForm()
    
    return render(request, 'App_user/registro.html', {'form': form})

def loginWeb(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("../home")
            else:
                return render(request, 'App_user/login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
    
    return render(request, 'App_user/login.html', {'form': form})
    
def home(request):
    return render(request, "App_user/home.html")