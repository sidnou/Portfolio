from django.shortcuts import render
# TODO: A faire plus utile et optimisé
# MENUS = {
#     "Experiences":"{% url 'experiences' %}",
#     "Competences":"{% url 'Competences' %}",
#     "Certifications":"",
#     "Formations":"",
#
# }

VERSION = "0.0.01"

# Create your views here.
def accueil(request):
    context = {
        "Titre" : "Portfolio",
        "Version" : VERSION,

        }
    return render(request,'core/index.html',context)


def a_propos(request):
    context = {
        "Titre": "À Propos",
        "Version": VERSION
    }
    return render(request,'core/a-propos.html',context)


def experiences(request):
    context = {
        "Titre": "Expériences",
        "Version": VERSION
    }
    return render(request,'core/experiences.html',context)


def competences(request):
    context = {
        "Titre": "Compétences",
        "Version": VERSION
    }
    return render(request, 'core/competences.html', context)


def loisirs(request):
    context = {
        "Titre": "Loisirs",
        "Version": VERSION
    }
    return render(request, 'core/loisirs.html', context)


def hobbies(request):
    context = {
        "Titre": "Hobbies",
        "Version": VERSION
    }
    return render(request, 'core/hobbies.html', context)


def certificats(request):
    context = {
        "Titre": "Certificats",
        "Version": VERSION
    }
    return render(request, 'core/certificats.html', context)


def formations(request):
    context = {
        "Titre": "Formations",
        "Version": VERSION
    }
    return render(request, 'core/formations.html', context)