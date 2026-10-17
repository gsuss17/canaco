from django.contrib.auth.decorators import login_required, user_passes_test 
from django.shortcuts import render

def es_operador(user): 
    return user.is_authenticated and user.is_staff and user.is_active 

operador_required = user_passes_test(es_operador, login_url='home:login')

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