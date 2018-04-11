from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from .models import Profiel


class ProfielUpdate(LoginRequiredMixin, UpdateView):
    model = Profiel
    template_name = 'accounts/profiel.html'
