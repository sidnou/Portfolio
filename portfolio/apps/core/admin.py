from django.contrib import admin
from .models import Experience, Competences


# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    ...

@admin.register(Competences)
class CompetencesAdmin(admin.ModelAdmin):
    ...