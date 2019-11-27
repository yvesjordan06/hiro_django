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
    description = models.CharField(max_length=500)
    taches = models.ManyToManyField(Tache)

    def __str__(self):
        return self.intitule

    def __unicode__(self):
        return self.intitule


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

    def nombres_de_taches(self) -> int:
        return self.taches.all().count()

    def est_visible(self) -> bool:
        return bool(self.taxation)

    est_visible.boolean = True


