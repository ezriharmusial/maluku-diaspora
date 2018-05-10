from import_export.fields import Field
from import_export import resources
from .models import Adres


class AdresResource(resources.ModelResource):
    straatnaam = Field()
    postcode = Field()
    plaatsnaam = Field()
    deelgemeente = Field()
    provincie = Field()
    volledig_adres = Field()
    bewoond = Field()
    bewoners = Field()

    class Meta:
        model = Adres
        fields = (
            'id',
            'slug',
            'bewoond',
            'bewoners',
            'vernomen_adres',
            'straatnaam',
            'huisnummer',
            'toevoeging',
            'postcode',
            'plaatsnaam',
            'deelgemeente',
            'provincie'
        )
        export_order = (
            'id',
            'slug',
            'bewoond',
            'bewoners',
            'vernomen_adres',
            'straatnaam',
            'huisnummer',
            'toevoeging',
            'postcode',
            'plaatsnaam',
            'deelgemeente',
            'provincie'
        )

    def dehydrate_bewoond(self, Adres):
        return '%s' % (Adres.bewoond())

    def dehydrate_bewoners(self, Adres):
        return '%s' % (Adres.bewoners())

    def dehydrate_postcode(self, Adres):
        return Adres.postcode.postcode

    def dehydrate_straatnaam(self, Adres):
        return '%s' % (Adres.straatnaam())

    def dehydrate_plaatsnaam(self, Adres):
        return '%s' % (Adres.plaatsnaam())

    def dehydrate_deelgemeente(self, Adres):
        return '%s' % (Adres.deelgemeente())

    def dehydrate_provincie(self, Adres):
        return '%s' % (Adres.provincie())
