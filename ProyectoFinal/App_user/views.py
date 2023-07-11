from django.shortcuts import render, redirect
from .forms import RegistroForm, UserEditForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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

@login_required    
def home(request):
    return render(request, "App_user/home.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("../")

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return redirect('../home')
        
        else:
            form = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name} )
            return render(request, 'App_user/editarPerfil.html', {"form": form })
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'App_user/editarPerfil.html', {"form": form})

