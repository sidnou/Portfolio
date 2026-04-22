from django.contrib import admin
from .models import Experience, Competence, Langue


# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    ...

@admin.register(Competence)
class CompetencesAdmin(admin.ModelAdmin):
    ...

@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    ...
