from django.conf import settings
from home.models import Categoria, Publicacion, Perfil

def global_categorias(request):
    return {
        'global_categorias': Categoria.objects.all().order_by('nombre'),
        'global_recientes': Publicacion.objects.filter(estado=Publicacion.ESTADO_PUBLICADO).order_by('-createdat')[:3],
        'categorias_header': Categoria.objects.all().order_by("nombre")
    }

def perfil_context(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.filter(user=request.user).first() # Ajusta 'user' si tu campo se llama 'fk_user' o similar
        return {'perfil_usuario': perfil}
    return {'perfil_usuario': None}

def google_analytics(request):
    # Si DEBUG es True (desarrollo local), no envía el ID
    if settings.DEBUG:
        return {'GA_MEASUREMENT_ID': None}

    return {
        'GA_MEASUREMENT_ID': getattr(settings, 'GA_MEASUREMENT_ID', None)
    }