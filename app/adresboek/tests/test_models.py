from django.test import TestCase

# Create your tests here.

from adresboek.models import Adres, Postcode


class PostcodeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Postcode.objects.create(
            postcode='4142EA',
            straatnaam='Populierstraat',
            plaatsnaam='Leerdam',
            deelgemeente='Leerdam',
            provincie='ZH',
            breedtegraad='51.8895226862398',
            lengtegraad='5.0767838385945'
        )

    def test_expected_object_name_is_postcode(self):
        postcode = Postcode.objects.get(postcode='4142EA')
        self.assertEquals(
            str(postcode),
            '4142EA'
        )


class AdresModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Postcode.objects.create(
            postcode='0000AA',
            straatnaam='--',
            plaatsnaam='--',
            deelgemeente='--',
            provincie='FR',
            breedtegraad='0',
            lengtegraad='0',
        )

        Postcode.objects.create(
            postcode='4142EA',
            straatnaam='Populierstraat',
            plaatsnaam='Leerdam',
            deelgemeente='Leerdam',
            provincie='ZH',
            breedtegraad='51.8895226862398',
            lengtegraad='5.0767838385945',
        )

        Adres.objects.create(
            slug='4142EA13',
            vernomen_bewoners='"Mevr. Harmusial (Francien)"',
            vernomen_adres='Populierstraat 13',
            postcode_id=2,
            huisnummer=13,
            toevoeging='',
            in_de_wijk=1,
            compleet=1,
        )

        Adres.objects.create(
            slug='4142EA15',
            vernomen_bewoners='',
            vernomen_adres='Populierstraat 15',
            postcode_id=2,
            huisnummer=15,
            toevoeging='',
            in_de_wijk=1,
            compleet=1,
        )

        Adres.objects.create(
            slug='',
            vernomen_bewoners='Pietje',
            vernomen_adres='Ergens aan de Straatweg',
            postcode_id=1,
            huisnummer=0,
            toevoeging='',
            in_de_wijk=0,
            compleet=0,
        )

        Adres.objects.create(
            slug='',
            vernomen_bewoners='Jan en Antje',
            vernomen_adres='',
            postcode_id=1,
            huisnummer=0,
            toevoeging='',
            in_de_wijk=0,
            compleet=0,
        )

    # if self.compleet:
    def test_expected_volledig_adres_vernomen(self):
        adres = Adres.objects.get(slug='4142EA13')
        self.assertEquals(
            adres.volledig_adres(),
            'Populierstraat 13, 4142EA Leerdam'
        )

    # elif self.vernomen_adres:
    def test_expected_volledig_adres_compleet(self):
        adres = Adres.objects.get(vernomen_adres='Ergens aan de Straatweg')
        self.assertEquals(
            adres.volledig_adres(),
            'Ergens aan de Straatweg, Leerdam'
        )

    # else:
    def test_expected_volledig_adres_onbekend(self):
        adres = Adres.objects.get(vernomen_bewoners='Jan en Antje')
        self.assertEquals(
            adres.volledig_adres(),
            'Adres Onbekend'
        )

    def test_get_absolute_url(self):
        adres = Adres.objects.get(slug='4142EA13')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(
            adres.get_absolute_url(),
            '/adressen/details/4142EA13/'
        )

    def test_adres_urlformat(self):
        adres = Adres.objects.get(slug='4142EA13')
        self.assertEquals(
            adres.adres_urlformat(),
            'Populierstraat%2013,%204142EA%20Leerdam'
        )

