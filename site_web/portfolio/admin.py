from django.contrib import admin
from .models import Profil,Experience,Competence,Hobbie,Language
# Register your models here.
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    pass
