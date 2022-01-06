from django.urls import path
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [

    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('achat/', views.achat, name='achat'),
    path('location', views.location, name='location'),
    path('vente', views.vente, name='vente'),
    #path('result', views.result, name='result'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)