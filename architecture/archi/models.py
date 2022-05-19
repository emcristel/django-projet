from django.db import models


class Architecte(models.Model):
    archit= models.CharField(null=True, blank=True, max_length=30)
    style= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.archit

class Oeuvre(models.Model):

    nom = models.CharField(null=True, blank=True, max_length=60)
    creation = models.DateField (blank=True, null=True)
    localisation = models.CharField(null=True, blank=True, max_length=30)
    type_oeuvre = models.CharField(null=True, blank=True, max_length=500)
    architecte = models.ForeignKey(Architecte, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


    def dico(self):
        return{"nom": self.nom, "creation": self.creation, "localisation": self.localisation, "type_oeuvre": self.type_oeuvre, "architecte": self.architecte}