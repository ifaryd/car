from django.contrib import admin


from . models import Carburant, Couleur, Couleur_intertieur, Etat, Lieu, Matiere_interieur, Transmission, Voiture, Marque, Modele

admin.site.register(Voiture)
admin.site.register(Marque)
admin.site.register(Modele)
admin.site.register(Etat)
admin.site.register(Lieu)
admin.site.register(Couleur)
admin.site.register(Couleur_intertieur)
admin.site.register(Matiere_interieur)
admin.site.register(Transmission)
admin.site.register(Carburant)
