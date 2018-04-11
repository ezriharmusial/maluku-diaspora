from django.urls import path
from django.urls import include, path

from . import views


urlpatterns = [
    path('accounts/profiel/<slug:slug>', views.ProfielUpdate.as_view(), name='profiel'),
    path('accounts/', include('django.contrib.auth.urls')),
]
