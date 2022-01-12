from django.db import models
import datetime

from django.db.models.base import Model
from multiselectfield import MultiSelectField
from django.db.models.fields import BooleanField, TextField

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

    MY_OP = ((1, 'Ecran de bord'),
              (2, 'Camera de recule'),
              (3, 'Demarrage start/Stop'),
              (4, 'Toit panoramique'),
              (5, 'Abs'),
              (6, 'Capteur avant et arrière'),
              (7, 'siège ventilé'),
              (8, 'siège climatisé'),
              
            )

    
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    marque             = models.ForeignKey('Marque', on_delete=models.CASCADE, null=True, blank=True)
    modele             = models.ForeignKey('Modele', on_delete=models.CASCADE, null=True, blank=True)
    couleur            = models.ForeignKey('Couleur', on_delete=models.CASCADE, null=True, blank=True)
    couleur_intertieur = models.ForeignKey('Couleur_intertieur', on_delete=models.CASCADE, null=True, blank=True)
    matiere_interieur  = models.ForeignKey('Matiere_interieur', on_delete=models.CASCADE, null=True, blank=True)

    etat               = models.ForeignKey('Etat', on_delete=models.CASCADE, null=True, blank=True)
    lieu               = models.ForeignKey('Lieu', on_delete=models.CASCADE, null=True, blank=True)
    transmission       = models.ForeignKey('Transmission', on_delete=models.CASCADE, null=True, blank=True)
    carburant          = models.ForeignKey('Carburant', on_delete=models.CASCADE, null=True, blank=True)
    annee              = models.IntegerField(choices=YEAR_CHOICES)
    prix               = models.CharField(max_length=300)
    kilometrage        = models.IntegerField()
    opt                = MultiSelectField(choices=MY_OP)
    photo_face         = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_longueur1    = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_longueur2    = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_arriere      = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_tableau      = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_option1      = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_option2      = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_option3      = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_moteur       = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_carte_grise  = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    photo_assurance    = models.ImageField(upload_to='media/images/', default="app/static/images/logo-light.png", null=True, blank=True)
    description        = models.TextField()
    date_ajout         = models.DateField()
    toit_ouvrant = models.BooleanField(default=False)
    def __str__(self):
        return str(self.marque)+ " " + str(self.modele) + " " + str(self.date_ajout)



class Contact(models.Model):
    nom= models.CharField(max_length=225)
    email= models.EmailField()
    telephone= models.CharField(max_length=225)
    message=models.TextField()

    def __str__(self):
        return self.email