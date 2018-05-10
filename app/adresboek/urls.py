from django.urls import path
from . import views

# Register our App name
app_name = 'adresboek'


#Dynamic Pages Adressem
urlpatterns = [
    # ex /adressen
    path('', views.AdresListView.as_view(), name='adres_lijst'),
    path('adressen/toevoegen/', views.AdresCreate.as_view(), name='adres_toevoegen'),
    path('adressen/bewerken/<slug:slug>/', views.AdresUpdate.as_view(), name='adres_bewerken'),
    path('adressen/verwijderen/<slug:slug>/', views.AdresDelete.as_view(), name='adres_verwijderen'),
    # ex /adresboek/adres/4142EA/13
    path('adressen/details/<slug:slug>/', views.AdresDetailView.as_view(), name='adres_details'),
]
