from django.db import models


# Create your models here.
class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projets/")
    url = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Profil(models.Model):
    photo = models.ImageField(upload_to="profil/")
    description = models.TextField()

    def __str__(self):
        return "Profil"
