from django.db import models


class Architecte(models.Model):
    archit= models.CharField(max_length=30)
    style= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.archit

class Table(models.Model):

    nom= models.CharField(max_length=60)
    creation= models.DateField(blank=True, null=True)
    localisation= models.CharField(max_length=30)
    type_oeuvre= models.TextField(null=True, blank=True)
    architecte = models.ForeignKey(Architecte, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.nom} a été créé le {self.creation} à {self.localisation}. C'est un {self.type_oeuvre}"
        return chaine
