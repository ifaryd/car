from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *

def index(request):
    voiture=Voiture.objects.all().order_by('-id') [:4]
    marque= Marque.objects.all().order_by('marque')
    modele= Modele.objects.all().order_by('modele')
    etat= Etat.objects.all().order_by('etat')
    transmission= Transmission.objects.all().order_by('transmission')
    annee= YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r))
    data = {
        'voiture':voiture,
        'marque':marque,
        'modele':modele,
        'etat':etat,
        'transmission':transmission,
        'annee':annee,
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

def achat(request):
    voiture=Voiture.objects.all().order_by('-id')

    paginator = Paginator(voiture, 15)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1     
    try:
        voiture = paginator.page(page)
    except(EmptyPage, InvalidPage):
        voiture = paginator.page(paginator.num_pages)

    data = {
        'voiture':voiture,
        'paginator':paginator,
    }
    return render(request, 'achat.html', data)