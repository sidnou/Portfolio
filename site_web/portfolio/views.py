from django.shortcuts import render
from django.views.generic import TemplateView

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
class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        'auteur': AUTEUR,
        "version": VERSION,
        "titre": "Portfolio",
        "profils": Profil.objects.all(),
        "languages": Language.objects.all(),
        "competences": Competence.objects.all(),
        "experiences": Experience.objects.all(),
        "hobbies": Hobbie.objects.all(),
    })
        return context
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())