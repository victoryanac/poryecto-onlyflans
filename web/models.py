from django.db import models
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User



# Create your models here.


# Clases  de modelos que se van a utilizar en la base de datos
class Flan (models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True) # infresa identificador por defecto para no tener que hacerlo a mano
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=False)
    image = models.URLField () # campo para la url
    slug = models.SlugField(max_length=255, unique=True, blank=True) 
    is_private = models.BooleanField(default=False) # si es privado o no
    price = models.DecimalField(max_digits=10, decimal_places=0, default=100) # campo para el precio
    alto_calorias = models.BooleanField(default=False) # campo para las calorias

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    # metodo para mostrar el nombre del modelo en el administrador de django
    def __str__(self):
        return self.name

class Contacto(models.Model):
    contactForm_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField(blank=False)
    customer_name = models.CharField(max_length=50, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.customer_name
    

# Clase para agregar flan a favoritos
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'flan')  # Evita duplicados

    def __str__(self):
        return f"{self.user.username} favorited {self.flan.name}"



