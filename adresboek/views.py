from django.views import generic

from .models import Adres


# Create your views here.
class AdresListView(generic.ListView):
    model = Adres
    template_name = 'adresboek/adres_lijst.html'


class AdresDetailView(generic.DetailView):
    model = Adres
    template_name = 'adresboek/adres_details.html'
