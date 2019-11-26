from django.urls import path
from . import views

from btpp.views import AnnoncesViewSet
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'annonces', AnnoncesViewSet)
urlpatterns = [
   url(r'^', include(router.urls)),
    
]
