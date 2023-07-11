from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    
    else: 
        form = UserCreationForm()
    return render(request, 'App_user/registro.html', {'form': form})

def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../home")
        else:
            return render(request, 'App_user/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'App_user/login.html')
    
def home(request):
    return render(request, "App_user/home.html")