from btpp.models import *
from rest_framework import serializers

class AnnoncesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = '__all__'