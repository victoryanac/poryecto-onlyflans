"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import index
from web.views import welcome 
from web.views import about
from web.views import contact_view
from web.views import contact_view_exito
from django.urls import include, path # se importa include y path de django.urls
from web.views import flan_detail
from web import views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('welcome/', welcome , name='welcome'),
    path('contacto_existoso/', contact_view_exito, name='contact_view_exito'),
    path('contact_form/', contact_view, name='contact_form'),
    path('accounts/', include('django.contrib.auth.urls')), # se incluyen las urls de autenticacion de django
    path('flan/<int:flan_id>/', flan_detail, name='flan_detail'),
    
    path('add_to_favorites/<int:flan_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:flan_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites, name='favorites'),

]