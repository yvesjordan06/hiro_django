from django.urls import path
from . import views

from btpp.views import *
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'annonces', AnnoncesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'taches', TachesViewSet)
router.register(r'metier', MetiersViewSet)
urlpatterns = [
   url(r'^', include(router.urls)),
    
]
