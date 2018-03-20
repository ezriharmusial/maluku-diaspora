from .models import Adres, Postcode
from django import forms
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from django.utils.safestring import mark_safe

import csv



# Custom Headers & Titles 
class AdresboekAdminSite(admin.AdminSite):
    site_header = "Adresboek Beheersysteem"
    site_title = "Adresboek Beheersysteem"
    index_title = "Welkom in het Adresboek Beheersysteem"


# Seperate Admin Section
adresboek_admin_site = AdresboekAdminSite(name='adresboek_admin')


# Object Admin Classes
class AdresAdmin(admin.ModelAdmin):
    change_list_template = "adresboek/import_csv_changelist.html"
    list_filter = (
        "in_de_wijk",
    )

    list_display = (
        "vernomen_bewoners",
        "straatnaam",
        "huisnummer",
        "toevoeging",
        "postcode",
        "plaatsnaam",
        "deelgemeente",
        "in_de_wijk",
    )

    readonly_fields = ["id", "locatie_foto_display"]
    # raw_id_fields = ["postcode"]

    def locatie_foto_display(self, obj):
        return mark_safe(
            '<img src="{url}" width="150" height="150" class="lazyload" />'.format(
                url=obj.static_locatie_foto_url(),
                width=obj.locatie_foto.width,
                height=obj.locatie_foto.height,
            )
        )


class PostcodeAdmin(admin.ModelAdmin):
    change_list_template = "adresboek/import_csv_changelist.html"

    list_display = (
        "postcode",
        "straatnaam",
        "plaatsnaam",
        "deelgemeente",
        "provincie",
    )


adresboek_admin_site.register(Adres, AdresAdmin)
adresboek_admin_site.register(Postcode, PostcodeAdmin)
