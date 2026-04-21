from django.urls import path
from . import views
urlpatterns = [
    path('',views.accueil,name="accueil"),
    path("a-propos/",views.a_propos,name="a-propos"),
    path("experiences/",views.experiences,name="experiences"),
    path("competences/",views.competences,name='competences'),
    path("loisirs/",views.loisirs,name='loisirs'),
    path("hobbies/",views.hobbies,name='hobbies'),
    path('certificats/',views.certificats,name="certificats"),
    path('formations/',views.formations,name='formations'),
]
