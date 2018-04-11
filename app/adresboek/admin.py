from .models import Adres, Postcode
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
        'volledig_adres',
        'in_de_wijk',
        'compleet',
    )

    fieldsets = (
        ('Adres Gegevens', {
            'fields': (
                'vernomen_bewoners',
                'volledig_adres',
                'postcode',
                (
                    'huisnummer',
                    'toevoeging',
                ),
            ),
        }),
        ('Maps', {
            'fields': (
                'google_streetview_image_html',
                # 'google_streetview_image_url',
                # 'google_streetview_image',
                'google_maps_image_html',
                # 'google_maps_image_url',
                # 'google_maps_image',
            ),
        }),
    )

    readonly_fields = [
        'slug',
        'vernomen_bewoners',
        'google_streetview_image_html',
        'google_streetview_image_url',
        'google_streetview_image',
        'google_maps_image_html',
        'google_maps_image_url',
        'google_maps_image',
        'straatnaam',
        'volledig_adres',
    ]
    # raw_id_fields = ['postcode']


class PostcodeAdmin(admin.ModelAdmin):
    list_display = (
        'straatnaam',
        'postcode',
        'plaatsnaam',
        'deelgemeente',
        'provincie',
    )

    fields = (
        'straatnaam',
        'postcode',
        (
            'plaatsnaam',
            'deelgemeente',
        ),
        'provincie',
    )


adresboek_admin_site.register(Adres, AdresAdmin)
adresboek_admin_site.register(Postcode, PostcodeAdmin)
