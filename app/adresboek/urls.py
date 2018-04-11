from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

# Register our App name
app_name = 'adresboek'

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'adressen', views.AdresJsonViewSet)
# router.register(r'users', views.UserViewSet)

#Dynamic Pages Postcodes
urlpatterns = [
]

#Dynamic Pages Adressem
urlpatterns += [
    # ex /adressen
    path('', views.AdresListView.as_view(), name='adres_lijst'),
    path('adressen/toevoegen/', views.AdresCreate.as_view(), name='adres_toevoegen'),
    path('adressen/bewerken/<slug:slug>/', views.AdresUpdate.as_view(), name='adres_bewerken'),
    path('adressen/verwijderen/<slug:slug>/', views.AdresDelete.as_view(), name='adres_verwijderen'),
    # ex /adresboek/adres/4142EA/13
    path('adressen/details/<slug:slug>/', views.AdresDetailView.as_view(), name='adres_details'),
]
