from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets


# Create your views here.

class AnnoncesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Annonce.objects.all().order_by('-date_post')
    serializer_class = AnnoncesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-created_on')
    serializer_class = UsersSerializer


class MetiersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Metier.objects.all().order_by('-intitule')
    serializer_class = MetiersSerializer


class TachesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tache.objects.all().order_by('-intitule')
    serializer_class = TachesSerializer
