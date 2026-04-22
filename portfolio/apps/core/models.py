from random import choices

from django.db import models
from django.db.models import Model


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





class Competence(models.Model):
    experiences = models.ManyToManyField(Experience)
    competence = models.CharField(max_length=50)




class Certificat(models.Model):
    date = models.DateField()
    nom_certificat = models.CharField()


class Formation(models.Model):
    date = models.DateField()
    nom_formation = models.CharField(max_length=50)


class Langue(models.Model):
    LANGUE = [
        ("Allemand", "Allemand"),
        ("Anglais", "Anglais"),
        ("Arabe", "Arabe"),
        ("Bengali", "Bengali"),
        ("Chinois", "Chinois"),
        ("Coréen", "Coréen"),
        ("Espagnol", "Espagnol"),
        ("Français", "Français"),
        ("Hindi", "Hindi"),
        ("Indonésien", "Indonésien"),
        ("Italien", "Italien"),
        ("Japonais", "Japonais"),
        ("Néerlandais", "Néerlandais"),
        ("Persan", "Persan"),
        ("Polonais", "Polonais"),
        ("Portugais", "Portugais"),
        ("Russe", "Russe"),
        ("Turc", "Turc"),
        ("Ukrainien", "Ukrainien"),
        ("Urdu", "Urdu"),
        ("Swahili", "Swahili"),
        ("Tamoul", "Tamoul"),
        ("Thaï", "Thaï"),
        ("Vietnamien", "Vietnamien"),
    ]
    NIVEAU = [
        ("A1", "A1 - Débutant"),
        ("A2", "A2 - Élémentaire"),
        ("B1", "B1 - Intermédiaire"),
        ("B2", "B2 - Intermédiaire avancé"),
        ("C1", "C1 - Avancé"),
        ("C2", "C2 - Maîtrise"),
    ]
    langue = models.CharField(max_length=50,choices=LANGUE)
    niveau = models.CharField(max_length=50, choices=NIVEAU)

    def __str__(self):
        return self.langue
class Document(models.Model):
    TYPE_DOC = [
        ('CV','CV'),
        ('Carte Visite','Carte Visite')
    ]
    type_document = models.CharField(max_length=50,choices=TYPE_DOC,default="CV")

    document = models.FileField(upload_to=f"Documents/")

# TODO : Injecter les permis français automatiquement lors de la première creation de la base de donnée
class Permis(models.Model):
    permis = models.CharField(max_length=50)


class RenseignementsPersonnel(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=250)
    numero_telephone = models.CharField(max_length=14)
    e_mail = models.EmailField()
    permis = models.ManyToManyField(Permis)
    lien_reseau_social = models.URLField()

