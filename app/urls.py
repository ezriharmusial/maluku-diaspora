"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from adresboek.admin import adresboek_admin_site


urlpatterns = [
    path('adresboek/', include('adresboek.urls')),
    path('systeem-beheer/', admin.site.urls),
    path('adresboek-beheer/', adresboek_admin_site.urls),
]

admin.site.site_header = "Diaspora Beheersysteem"
admin.site.site_title = "Diaspora Beheersysteem"
admin.site.index_title = "Welkom in het Beheersysteem"
