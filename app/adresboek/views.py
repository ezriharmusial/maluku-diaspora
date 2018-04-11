from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

from .models import Adres


# Create your views here.
class AdresListView(LoginRequiredMixin, generic.ListView):
    model = Adres
    template_name = 'adresboek/adres_lijst.html'


class AdresDetailView(LoginRequiredMixin, generic.DetailView):
    model = Adres
    template_name = 'adresboek/adres_details.html'


class AdresCreate(CreateView):
    model = Adres
    fields = [
        'vernomen_bewoners',
        'vernomen_adres',
        'huisnummer',
        'toevoeging',
        'postcode',
    ]


class AdresUpdate(UpdateView):
    model = Adres
    fields = [
        'vernomen_bewoners',
        'vernomen_adres',
        'huisnummer',
        'toevoeging',
        'postcode',
    ]


class AdresDelete(DeleteView):
    model = Adres
    success_url = reverse_lazy('adresboek:adres_lijst')
