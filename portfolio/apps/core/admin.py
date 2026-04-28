from django.contrib import admin
from .models import Experience, Competence, Langue, Document, RenseignementsPersonnel, DescriptionPersonnel


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


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(RenseignementsPersonnel)
class RenseignementsPersonnelAdmin(admin.ModelAdmin):
    ...


@admin.register(DescriptionPersonnel)
class DescriptionPersonnelAdmin(admin.ModelAdmin):
    ...
