from django.db import models


# Create your models here.

class TypePoste(models.TextChoices):
    CDI = 'CDI','CDI'
    CDD = 'CDD','CDD'
    MISSION = 'MISSION','MISSION'
    STAGE = 'STAGE','STAGE'

class Experience(models.Model):
    entreprise = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    poste = models.CharField(max_length=50)
    fonctions_roles = models.CharField(max_length=250)
    type_poste = models.CharField(max_length=25, choices=TypePoste)

    def __str__(self):
        return f"{self.poste}"


class Competence(models.Model):
    experiences = models.ManyToManyField(Experience,blank=True)
    competence = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.competence}"


class Certificat(models.Model):
    date = models.DateField()
    nom_certificat = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} {self.nom_certificat}"


# Table Formation
class Formation(models.Model):
    date = models.DateField()
    nom_formation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date} {self.nom_formation}"

#  TODO : A simplifier avec une class et TextChoices
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
    langue = models.CharField(max_length=50, choices=LANGUE)
    niveau = models.CharField(max_length=50, choices=NIVEAU)

    def __str__(self):
        return self.langue

#  TODO : A simplifier avec une class et TextChoices

class Document(models.Model):
    TYPE_DOC = [
        ('CV', 'CV'),
        ('Carte Visite', 'Carte Visite')
    ]
    type_document = models.CharField(max_length=50, choices=TYPE_DOC, default="CV")

    document = models.FileField(upload_to=f"Documents/")


# TODO : Injecter les permis français automatiquement lors de la première creation de la base de donnée
class Permis(models.Model):
    permis = models.CharField(max_length=50, null=True,unique=True,blank=True)


class Hobbie(models.Model):
    hobbies = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Loisir(models.Model):
    loisirs = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class RenseignementsPersonnel(Hobbie, Loisir):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=250)
    numero_telephone = models.CharField(max_length=14)
    e_mail = models.EmailField(unique=True)
    permis = models.ManyToManyField(Permis)
    linkedin = models.URLField(unique=True, blank=True)
    facebook = models.URLField(unique=True, blank=True)
    site_web = models.URLField(unique=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class DescriptionPersonnel(models.Model):
    renseignements_personnel = models.ForeignKey(RenseignementsPersonnel, on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.renseignements_personnel} {self.description}"
