from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.wiki_title, name='wiki-title'),
    path('wiki/<str:t>/edit/', views.wiki_edit, name='wiki-edit'),
    path('new/', views.wiki_new, name='wiki-new'),
    path('search/', views.wiki_search, name='wiki-search'),
    path('random/', views.wiki_random, name='wiki-random'),
    #path('teste/', views.teste, name='teste'),
]