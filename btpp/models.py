from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Taxation(models.Model):
    intitule: str = models.CharField(max_length=200)
    prix: int = models.IntegerField()
    description: str = models.CharField(max_length=500)

    def __str__(self):
        return self.intitule + ' ' + str(self.prix) + ' CFA'

    def __unicode__(self) -> int:
        return self.prix


class Tache(models.Model):
    intitule: str = models.CharField(max_length=200)
    description: str = models.CharField(max_length=500)

    def __str__(self):
        return self.intitule

    def __unicode__(self):
        return self.intitule


class Metier(models.Model):
    intitule = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    taches = models.ManyToManyField(Tache)

    def __str__(self):
        return self.intitule

    def __unicode__(self):
        return self.intitule


class Abonnement(models.Model):
    intitule = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    prix = models.BigIntegerField(default=0)

    def __str__(self):
        return self.intitule

    def __unicode__(self):
        return self.intitule


class User(models.Model):
    email = models.EmailField(max_length=75, blank=True, null=True)
    telephone = models.CharField(max_length=75, blank=False)
    password = models.CharField(null=False, blank=False, max_length=128)
    nom = models.CharField(max_length=42, null=False, blank=False)
    prenom = models.CharField(max_length=42, null=True, blank=True)
    ville = models.CharField(max_length=42, null=True)
    quartier = models.CharField(max_length=42, null=True)
    boite_postal = models.CharField(max_length=42, null=True, blank=False)
    est_entreprise = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    abonnement = models.ForeignKey(Abonnement, on_delete=models.SET_NULL, null=True, blank=True)
    metiers = models.ManyToManyField(Metier, blank=True)
    est_active = models.BooleanField(default=True)

    def taches(self):
        return Tache.objects.filter(metier__in=self.metiers.all())

    def __str__(self):
        return "{nom} {prenom} ({number})".format(
            nom=self.nom,
            prenom=self.prenom or '',
            number=self.telephone
        )

    def __unicode__(self):
        return self.telephone


class Annonce(models.Model):
    def __str__(self):
        return self.intitule

    def __unicode__(self):
        return self.intitule

    intitule = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_post = models.DateTimeField('date published', auto_now_add=True)
    est_complete = models.BooleanField(default=False)
    taches = models.ManyToManyField(Tache)
    taxation = models.ForeignKey(Taxation, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def nombres_de_taches(self) -> int:
        return self.taches.all().count()

    def est_visible(self) -> bool:
        return bool(self.taxation)

    est_visible.boolean = True

class Chat(models.Model):
    pass