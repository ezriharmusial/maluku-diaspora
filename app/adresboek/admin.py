from .models import Adres
from django.contrib import admin


# Custom Headers & Titles
class AdresboekAdminSite(admin.AdminSite):
    site_header = "Adresboek Beheersysteem"
    site_title = "Adresboek Beheersysteem"
    index_title = "Welkom in het Adresboek Beheersysteem"


# Seperate Admin Section
adresboek_admin_site = AdresboekAdminSite(name='adresboek_admin')


# Object Admin Classes
class AdresAdmin(admin.ModelAdmin):
    list_filter = (
        'in_de_wijk',
        'compleet',
    )

    list_display = (
        'vernomen_bewoners',
        'straatnaam',
        'huisnummer',
        'toevoeging',
        'postcode',
        'plaatsnaam',
        'in_de_wijk',
        'compleet',
    )

    fieldsets = (
        ('Adres Gegevens', {
            'fields': (
                'vernomen_bewoners',
                'straatnaam',
                (
                    'huisnummer',
                    'toevoeging',
                ),
                'postcode',
                (
                    'plaatsnaam',
                    'deelgemeente',
                ),
                'provincie',
            ),
        }),
        ('Maps', {
            'fields': (
                # 'google_streetview_image_html',
                # 'google_streetview_image_url',
                # 'google_streetview_image',
                # 'google_maps_image_html',
                # 'google_maps_image_url',
                # 'google_maps_image',
            ),
        }),
    )

    readonly_fields = [
        'slug',
    ]


adresboek_admin_site.register(Adres, AdresAdmin)
