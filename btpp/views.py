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
