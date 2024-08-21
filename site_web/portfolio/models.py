from django.db import models


# Create your models here.
class Profil(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    tel_mobile = models.CharField(max_length=11, blank=True, null=True)
    lien = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.nom} {self.prenom} {self.email}'


class Competence(models.Model):
    titre = models.CharField(max_length=25)
    niveau = models.IntegerField()

    def __str__(self):
        return f'{self.titre} {self.niveau}'


class Experience(models.Model):
    annee = models.DateField()
    entreprise = models.CharField(max_length=25)
    titre_poste = models.CharField(max_length=50)
    competence_entreprise = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.annee} {self.entreprise} {self.titre_poste}'


class Hobbie(models.Model):
    titre = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.titre}'


class Language(models.Model):
    langue = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.langue}'
