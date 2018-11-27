from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

# Create your models here.

class Persona(models.Model):
    run = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    vivienda = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=40)

    def __str(self):
        return "PERSONA"


class Mascotas(models.Model):

    fotografia = models.ImageField(upload_to = "Imagenes/")
    nombre_mascota = models.CharField(max_length = 20)
    raza_predominante = models.CharField(max_length = 20)
    descripcion = models.TextField()
    estado = models.CharField(max_length = 20)

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()
