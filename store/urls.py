from django.urls import path, include # importe les urls qui font partie du projet

from . import views # importe toutes les vues de l'appli


urlpatterns = [
    path('', views.listing), # toute vue qui contient une string vide est relié a index 'store/'
    path('<int:album_id>/', views.detail),
    path('search/', views.search),
]