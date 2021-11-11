from django.db import models
import datetime

from django.db.models.fields import BooleanField

class Marque(models.Model):
    marque = models.CharField(max_length=300)
    def __str__(self):
        return self.marque


class Modele(models.Model):
    modele = models.CharField(max_length=300)
    def __str__(self):
        return self.modele

class Transmission(models.Model):
    transmission = models.CharField(max_length=300)
    def __str__(self):
        return self.transmission

class Carburant(models.Model):
    carburant = models.CharField(max_length=300)
    def __str__(self):
        return self.carburant

class Matiere_interieur(models.Model):
    matiere_interieur = models.CharField(max_length=300)
    def __str__(self):
        return self.matiere_interieur

class Couleur_intertieur(models.Model):
    couleur_intertieur = models.CharField(max_length=300)
    def __str__(self):
        return self.couleur_intertieur

class Couleur(models.Model):
    couleur = models.CharField(max_length=300)
    def __str__(self):
        return self.couleur

class Etat(models.Model):
    etat = models.CharField(max_length=300)
    def __str__(self):
        return self.etat

class Lieu(models.Model):
    lieu = models.CharField(max_length=300)
    def __str__(self):
        return self.lieu

    
class Voiture(models.Model):
    id = models.BigAutoField(primary_key=True,)
    
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    marque = models.ForeignKey('Marque', on_delete=models.CASCADE, null=True, blank=True)
    modele = models.ForeignKey('Modele', on_delete=models.CASCADE, null=True, blank=True)
    couleur = models.ForeignKey('Couleur', on_delete=models.CASCADE, null=True, blank=True)
    couleur_intertieur = models.ForeignKey('Couleur_intertieur', on_delete=models.CASCADE, null=True, blank=True)
    matiere_interieur = models.ForeignKey('Matiere_interieur', on_delete=models.CASCADE, null=True, blank=True)

    etat = models.ForeignKey('Etat', on_delete=models.CASCADE, null=True, blank=True)
    lieu = models.ForeignKey('Lieu', on_delete=models.CASCADE, null=True, blank=True)
    transmission = models.ForeignKey('Transmission', on_delete=models.CASCADE, null=True, blank=True)
    carburant = models.ForeignKey('Carburant', on_delete=models.CASCADE, null=True, blank=True)
    annee = models.IntegerField(choices=YEAR_CHOICES)
    prix = models.CharField(max_length=300)
    kilometrage = models.IntegerField()
    photo_face = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_longueur1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_longueur2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_arriere = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_tableau = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option2 = models.ImageField(upload_to='images/',)
    photo_option3 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_option4 = models.ImageField(upload_to='images/', null=True, blank=True)    
    photo_option5 = models.ImageField(upload_to='images/', null=True, blank=True)    
    photo_moteur = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_carte_grise = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_assurance = models.ImageField(upload_to='images/', null=True, blank=True)
    toit_ouvrant = models.BooleanField(default=True)
    photo_defaut1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut3 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut4 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_defaut5 = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    date_ajout = models.DateField()
    def __str__(self):
        return str(self.marque)+ " " + str(self.modele) + " " + str(self.date_ajout)


