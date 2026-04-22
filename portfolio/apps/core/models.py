from django.db import models


# Create your models here.
class Experience(models.Model):

    TYPE_POSTE = [
        ('CDI','CDI'),
        ('CDD','CDD'),
        ('MISSION','MISSION'),
    ]
    entreprise = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True,blank=True)
    poste= models.CharField(max_length=25)
    fonctions_roles = models.CharField(max_length=250)
    type_poste = models.CharField(max_length=25,choices=TYPE_POSTE)



class Competences(models.Model):
    experiences = models.ManyToManyField(Experience)



class Certificat(models.Model):
    ...


class Formation(models.Model):
    ...


class Langue(models.Model):
    ...
