from django.shortcuts import render

from .models import Profil, Projet


def accueil(request):
    projets = Projet.objects.all().order_by("-date")
    profil = Profil.objects.first()
    return render(
        request, "portfolio/accueil.html", {"projets": projets, "profil": profil}
    )
