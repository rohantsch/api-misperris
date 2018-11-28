from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from registro.models import Persona, Mascotas
from registro.quickstart.serializers import MascotasSerializer, PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all().order_by('-pk')
    serializer_class = PersonaSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer