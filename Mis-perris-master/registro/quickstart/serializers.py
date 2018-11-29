from django.contrib.auth.models import User, Group
from registro.models import Persona, Mascotas
from rest_framework import serializers

class MascotasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascotas
        fields = ('fotografia', 'nombre_mascota','raza_predominante')

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('correo', 'run', 'nombre', 'telefono', 'fecha')
