from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('achat', views.achat, name='achat'),
    #path('result', views.result, name='result'),
    path('detail/<int:id>', views.detail, name='detail'),
]