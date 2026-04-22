from django.shortcuts import render

# Create your views here.
def accueil(request):
    context = {
        "Titre" : "Portfolio",
        "Version" : "0.0.01"
    }
    return render(request,'core/index.html',context)


def a_propos(request):
    context = {
        "Titre": "À Propos",
        "Version": "0.0.01"
    }
    return render(request,'core/a-propos.html',context)


def experiences(request):
    context = {
        "Titre": "Expériences",
        "Version": "0.0.01"
    }
    return render(request,'core/experiences.html',context)


def competences(request):
    context = {
        "Titre": "Compétences",
        "Version": "0.0.01"
    }
    return render(request, 'core/competences.html', context)


def loisirs(request):
    context = {
        "Titre": "Loisirs",
        "Version": "0.0.01"
    }
    return render(request, 'core/loisirs.html', context)


def hobbies(request):
    context = {
        "Titre": "Hobbies",
        "Version": "0.0.01"
    }
    return render(request, 'core/hobbies.html', context)


def certificats(request):
    context = {
        "Titre": "Certificats",
        "Version": "0.0.01"
    }
    return render(request, 'core/certificats.html', context)


def formations(request):
    context = {
        "Titre": "Formations",
        "Version": "0.0.01"
    }
    return render(request, 'core/formations.html', context)