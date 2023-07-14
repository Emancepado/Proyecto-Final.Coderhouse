from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm, UserEditForm, UserChangePassword, AvatarForm, productoForm
from .models import Avatar, producto as Productos 
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
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
                messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
                return redirect('../')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo "{field}": {error}')
    
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
    avatar = getAvatar(request)
    return render(request, "App_user/home.html",{"avatar": avatar})

@login_required
def logout_view(request):
    logout(request)
    return redirect("../")

@login_required
def editarPerfil(request):
    avatar = getAvatar(request)
    usuario = request.user
    user_basic_info = User.objects.get(id=usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            messages.success(request, '¡Perfil actualizado exitosamente!')
            return redirect('../home')
        else:
            form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo "{field}": {error}')
            return render(request, 'App_user/editarPerfil.html', {"form": form })
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'App_user/editarPerfil.html', {"form": form, "avatar": avatar})
    


@login_required
def editarContraseña(request):
    avatar = getAvatar(request)
    usuario = request.user 
    if request.method == 'POST':
        form = UserChangePassword(data=request.POST, user=usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada exitosamente.')
            return redirect('../editarPerfil')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo "{field}": {error}')
            return redirect('../editarContraseña')
    else: 
        form = UserChangePassword(user=usuario)
        return render(request, 'App_user/editarContraseña.html', {"form": form, "avatar": avatar})
    


@login_required
def editarAvatar(request):
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username = request.user)
            avatar = Avatar(user = usuario, image = form.cleaned_data['avatar'], description = form.cleaned_data['description'])
            avatar.save()
            messages.success(request, '¡Avatar actualizado exitosamente!')
            avatar = Avatar.objects.filter(user = request.user.id)
            return redirect('../editarPerfil')
    
    else:
        form = AvatarForm()
        avatar = getAvatar(request)
    return render(request, 'App_user/editarAvatar.html', {'form': form, 'avatar': avatar})




@login_required
def getAvatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    try:
        avatar = avatar[0].image.url
    
    except:
        avatar = None

    return avatar


@login_required
def crearProducto(request):
    avatar = getAvatar(request)
    if request.method == 'POST':
        miFormulario = productoForm(request.POST)
        if miFormulario.is_valid():
            producto = miFormulario.save(commit=False) 
            producto.usuario = request.user  
            producto.save()  
            messages.success(request, "Producto registrado exitosamente") 
            return redirect('productos')
    productos = Productos.objects.all()

    miFormulario = productoForm()
    return render(request, 'App_user/productos.html', {'form': miFormulario, "avatar": avatar, "productos": productos})




@login_required
def borrarProducto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)
    if producto.usuario == request.user:
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
    else:
        messages.error(request, 'No tienes permiso para eliminar este producto.')
    return redirect('productos')

