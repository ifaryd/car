from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm



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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html')
    form= ContactForm
    data= {'form': form}
    return render(request, 'contact.html', data)

def location(request):
    return render(request, 'location.html')

def vente(request):
    return render(request, 'vente.html')


# def result(request):
#     search_query = request.GET.get('search', '')
#     if  search_query:
#         marq = Marque.objects.filter(Q(marque__icontains = search_query))
#     else:
#         marq = Voiture.objects.filter()

#     data = {
#         'marq':marq
#     }
#     return render(request, 'result.html', data)

def achat(request):
    voiture=Voiture.objects.all().order_by('-id')
    marque= Marque.objects.all().order_by('marque')
    modele= Modele.objects.all().order_by('modele')
    etat= Etat.objects.all().order_by('etat')
    transmission= Transmission.objects.all().order_by('transmission')
    annee= YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r))


    search_query = request.GET.get('search')
    if  search_query:
        voiture = Voiture.objects.filter(Q(marque__marque__icontains = search_query) | Q(modele__modele__icontains = search_query))
    else:
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
        'marque':marque,
        'modele':modele,
        'etat':etat,
        'transmission':transmission,
        'annee':annee,
    }
    return render(request, 'achat.html', data)




def search(request):
    data = []
    if request.method == "POST":
        datas = request.POST
        datas._mutable = True
        
        voitures = Voiture.objects.filter()
            
        if 'marque' in datas:
            voitures = voitures.filter(marque__marque__in = datas.getlist("marque"))

        if 'modele' in datas:
            voitures = voitures.filter(modele__modele__in = datas.getlist("modele"))
            
        if 'etat' in datas:
            voitures = voitures.filter(etat__etat__in = datas.getlist("etat"))
            
        if 'transmission' in datas:
            voitures = voitures.filter(transmission__transmission__in = datas.getlist("transmission"))  
            
        if 'annee' in datas:
            voitures = voitures.filter(annee__in = datas.getlist("annee")) 
            
        if datas["search"] != "":
            voitures = voitures.filter(Q(marque__marque__icontains = datas["search"]) | Q(modele__modele__icontains = datas["search"])) 
            
        data = [x for x in voitures.values_list('id', flat=True)]
        print("-------------------------------", data)

    return JsonResponse({"data": data})
