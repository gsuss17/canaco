import os
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import Archivo, Categoria, Comentario, GaleriaPublicacion, Perfil, Publicacion 
from django.core.files.storage import default_storage 

def es_operador(user): 
    return user.is_authenticated and user.is_staff and user.is_active 

operador_required = user_passes_test(es_operador, login_url='home:login')


def sign_up(request): 
    if request.method == 'POST': 
        username = request.POST.get('username', '').strip() 
        email = request.POST.get('email', '').strip() 
        first_name = request.POST.get('first_name', '').strip() 
        apellido_paterno = request.POST.get('apellido_paterno', '').strip() 
        apellido_materno = request.POST.get('apellido_materno', '').strip() 
        password1 = request.POST.get('password1', '') 
        password2 = request.POST.get('password2', '') 

        if password1 != password2: 
            messages.error(request, 'Las contraseñas no coinciden.') 
            return redirect('home:sign_up') 

        if User.objects.filter(username=username).exists(): 
            messages.error(request, 'El nombre de usuario ya está en uso.') 
            return redirect('home:sign_up') 

        if User.objects.filter(email=email).exists(): 
            messages.error(request, 'El correo electrónico ya está registrado.') 
            return redirect('home:sign_up') 

        user = User.objects.create_user(username=username, email=email, password=password1) 
        user.first_name = first_name 
        user.last_name = ' '.join(filter(None, [apellido_paterno, apellido_materno])) 
        user.save() 
        perfil, _ = Perfil.objects.get_or_create(user=user) 
        perfil.apellido_paterno = apellido_paterno 
        perfil.apellido_materno = apellido_materno 
        perfil.save()
        messages.success(request, 'Tu cuenta ha sido creada con éxito. Ahora puedes iniciar sesión.') 
        return redirect('home:login') 
    
    return render(request, 'home/sign_up.html')

# --- VISTAS PÚBLICAS ---
def index(request):
    return render(request, "home/index.html")


def base(request):
    return render(request, "home/base.html")


def contactanos(request):
    return render(request, "home/contactanos.html")


def categoria(request):
    return render(request, "home/categoria.html")


def login(request):
    return render(request, "home/login.html")


def noticia(request):
    return render(request, "home/noticia.html")


def sign_up(request):
    return render(request, "home/sign_up.html")


# --- VISTAS PARA USUARIOS LOGUEADOS ---
@login_required
def perfil(request):
    return render(request, "home/perfil.html")

@login_required
def crear_publicacion(request):  # Asumiendo que usuarios normales pueden publicar
    return render(request, "home/crear_publicacion.html")

@login_required
def crud_cambiar_contrasena(request):
    return render(request, "home/crud_cambiar_contrasena.html")

@login_required
def crud_perfil(request):
    return render(request, "home/crud_perfil.html")


# --- VISTAS PARA OPERADORES / ADMIN ---
@operador_required
def crear_usuario(request):
    return render(request, "home/crear_usuario.html")


@operador_required
def crud_categorias(request):
    return render(request, "home/crud_categorias.html")


@operador_required
def crud_comentarios(request):
    return render(request, "home/crud_comentarios.html")


@operador_required
def crud_noticias(request):
    return render(request, "home/crud_noticias.html")


@operador_required
def crud_usuarios(request):
    return render(request, "home/crud_usuarios.html")


@operador_required
def editar_categoria(request):
    return render(request, "home/editar_categoria.html")