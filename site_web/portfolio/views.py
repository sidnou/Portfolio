from django.shortcuts import render

# Variables CONSTANT
AUTEUR = 'Jacques-a S'
VERSION = "0.0.1"


# Create your views here.
def portfolio(request):
    context = {
        'auteur': AUTEUR,
        "version": VERSION,
        "titre": "Portfolio"
    }

    return render(request, 'portfolio/index.html', context)
