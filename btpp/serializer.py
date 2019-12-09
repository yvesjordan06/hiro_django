from btpp.models import *
from rest_framework import serializers


class AnnoncesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Annonce
        fields = '__all__'


class TachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class MetiersSerializer(serializers.ModelSerializer):
    taches = TachesSerializer(many=True)

    class Meta:
        model = Metier
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    taches = TachesSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
