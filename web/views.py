from django.shortcuts import render,redirect
from .models import Flan # se importa el modelo Flan
from .forms import ContactForm # se importa el formulario de contacto
from django.contrib.auth.views import LoginView, LogoutView # se importan las vistas de login y logout del mmismo django
from django.contrib.auth.decorators import login_required # se importa el decorador de login requerido
from django.shortcuts import get_object_or_404 # se importa la funcion get_object_or_404 para obtener un objeto o devolver un 404
from .models import Favorite # se importa el modelo de favoritos




# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False) # se obtienen los flanes publicos
    return render(request, 'index.html', {'flanes':flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

#Muestra flanes privados solo en el caso de que el Welcome.html solo se pueda acceder si se esta logueado [@login_required]
@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True) # se obtienen los flanes privados
    return render(request, 'welcome.html', {'flanes':flanes_privados})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_view_exito')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':form})

def contact_view_exito(request):
    return render(request, 'contacto_exito.html', {})



# Clases de login y logout  imopirtabdas de django
class  CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'


#clase para pagina con detalle de flan para cada flan
def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    return render(request, 'flan_detail.html', {'flan':flan})


#Funciones  para agregar flan a favoritos
@login_required
def add_to_favorites(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    Favorite.objects.get_or_create(user=request.user, flan=flan)
    return redirect('favorites')

@login_required
def remove_from_favorites(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    Favorite.objects.filter(user=request.user, flan=flan).delete()
    return redirect('favorites')

@login_required
def favorites(request):
    user_favorites = Favorite.objects.filter(user=request.user).select_related('flan')
    return render(request, 'favorites.html', {'favorites': user_favorites})


