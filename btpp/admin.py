from django.contrib import admin
from btpp.models import *

# Register your models here.

class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'description', 'nombres_de_taches', 'taxation', 'est_visible', 'est_complete', 'lieu')
    list_filter = ['date_post']
    search_fields = ['intitule', 'description','lieu']
class MetierAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'description')
    search_fields = ['intitule', 'description']
class TaxationAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'description','prix')
    list_filter = ['prix']
class TacheAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'description')
    search_fields = ['intitule', 'description']
    

admin.site.register(Metier, MetierAdmin)
admin.site.register(Tache, TacheAdmin)
admin.site.register(Taxation, TaxationAdmin)
admin.site.register(Annonce, AnnonceAdmin)

