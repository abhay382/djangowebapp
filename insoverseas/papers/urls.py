from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),

     path('about/', views.about, name='aboutus'),
     path('contact/', views.contact, name='index'),
     path('factoury/', views.fatorytour, name='index'),

     path('boxes/', views.boxes, name='index'),
     path('cards/', views.cards, name='index'),
     path('christmas/', views.christmas, name='index'),
     path('gift/', views.gift, name='index'),
     path('journal/', views.journal, name='index'),
     path('lamp/', views.lamp, name='index'),
     path('papers/', views.papers, name='index'),
     path('papersbag/', views.papersbag, name='index'),
     path('seedpapers/', views.seedpapers, name='index'),



]