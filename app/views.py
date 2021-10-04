from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *

def index(request):
    voiture=Voiture.objects.all().order_by('-id') [:4]
    marque= Marque.objects.all().order_by('marque')
    modele= Modele.objects.all().order_by('modele')
    etat= Etat.objects.all().order_by('etat')
    data = {
        'voiture':voiture,
        'marque':marque,
        'modele':modele,
        'etat':etat,
    }
    return render(request, 'index.html', data)


def detail(request, id):
    voiture=Voiture.objects.get(pk=int(id))
    recent=Voiture.objects.all().order_by('-id') [:4]
    data = {
        'voiture':voiture,
        'recent':recent,

    }
    return render(request, 'detail.html', data)


def contact(request):
    return render(request, 'contact.html')