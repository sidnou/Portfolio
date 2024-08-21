from django.shortcuts import render
from .models import Profil,Competence,Experience,Hobbie,Language
# Variables CONSTANT
AUTEUR = 'Jacques-a S'
VERSION = "0.0.1"


# Create your views here.
def portfolio(request):
    context = {
        'auteur': AUTEUR,
        "version": VERSION,
        "titre": "Portfolio",
        "profils": Profil.objects.all(),
        "languages": Language.objects.all(),
        "competences": Competence.objects.all(),
        "experiences": Experience.objects.all(),
        "hobbies": Hobbie.objects.all(),
    }

    return render(request, 'portfolio/index.html', context)
