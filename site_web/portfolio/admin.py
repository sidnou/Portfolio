from django.contrib import admin
from .models import Profil, Experience, Competence, Hobbie, Language


# Register your models here.
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Hobbie)
class HobbieAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
