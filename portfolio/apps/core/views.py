from django.shortcuts import render
from .models import Experience, Competence, Langue, Hobbie, Loisir, Formation, Permis, Certificat, \
    RenseignementsPersonnel, DescriptionPersonnel

# TODO: A faire plus utile et optimisé
MENUS = (
    {"url":"accueil","nom":"Accueil"},
    {"url":'experiences' ,"nom":"Experiences"},
    {"url":'competences' ,"nom":"Competences"},
    {"url":'cv',"nom":"CV"},
    {"url":'a-propos','nom':"À Propos"}
)

VERSION = "0.0.01"

# Create your views here.
def accueil(request):
    context = {
        "Titre" : "Portfolio",
        "Version" : VERSION,
        'Menus': MENUS

        }
    return render(request,'core/index.html',context)


def a_propos(request):
    context = {
        "Titre": "À Propos",
        "Version": VERSION,
        'Menus': MENUS,
        'A_propos' : RenseignementsPersonnel.objects.all(),
        "Descriptions_perso" :DescriptionPersonnel.objects.all(),
        'Permis': Permis.objects.all(),
    }
    return render(request,'core/a-propos.html',context)


def experiences(request):
    context = {
        "Titre": "Expériences",
        "Version": VERSION,
        'Menus': MENUS,
        'Experiences': Experience.objects.all()
    }
    return render(request,'core/experiences.html',context)


def competences(request):
    context = {
        "Titre": "Compétences",
        "Version": VERSION,
        'Menus': MENUS,
        'Competences': Competence.objects.all()
    }
    return render(request, 'core/competences.html', context)


def loisirs(request):
    context = {
        "Titre": "Loisirs",
        "Version": VERSION,
        'Menus': MENUS,
        'Loisirs':Loisir.objects.all(),
    }
    return render(request, 'core/loisirs.html', context)


def hobbies(request):
    context = {
        "Titre": "Hobbies",
        "Version": VERSION,
        'Menus': MENUS,
        'Hobbies':Hobbie.objects.all(),
    }
    return render(request, 'core/hobbies.html', context)


def certificats(request):
    context = {
        "Titre": "Certificats",
        "Version": VERSION,
        'Menus': MENUS,
        'Certificats': Certificat.objects.all(),
    }
    return render(request, 'core/certificats.html', context)


def formations(request):
    context = {
        "Titre": "Formations",
        "Version": VERSION,
        'Menus': MENUS,
        'Formation': Formation.objects.all()
    }
    return render(request, 'core/formations.html', context)

def cv(request):
    context = {
        "Titre": "CV",
        "Version": "0.0.01",
        'Menus': MENUS,
        'Langue':Langue.objects.all(),
    }

    return render(request,'core/cv.html',context)

