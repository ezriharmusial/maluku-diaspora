from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

import uuid


# Create your models here.
class Postcode(models.Model):
    class Meta:
        ordering = ['postcode']

    PROVINCIES = (
        ('DR', 'Drenthe'),
        ('FL', 'Flevoland'),
        ('FR', 'Friesland'),
        ('GE', 'Gelderland'),
        ('GR', 'Groningen'),
        ('LI', 'Limburg'),
        ('NB', 'Noord-Brabant'),
        ('NH', 'Noord-Holland'),
        ('OV', 'Overijssel'),
        ('UT', 'Utrecht'),
        ('ZE', 'Zeeland'),
        ('ZH', 'Zuid-Holland'),
    )

    postcode = models.CharField(
        max_length=6,
        blank=True,
        help_text='Formaat: 0000AA',
    )
    straatnaam = models.CharField(
        max_length=100,
        blank=True,
    )
    plaatsnaam = models.CharField(
        max_length=100,
        blank=True,
    )
    deelgemeente = models.CharField(
        max_length=100,
        blank=True,
    )
    provincie = models.CharField(
        max_length=2,
        choices=PROVINCIES,
        blank=True,
    )
    breedtegraad = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        null=True,
    )
    lengtegraad = models.DecimalField(
        max_digits=16,
        decimal_places=13,
        null=True,
    )
    wijzigings_datum = models.DateField(auto_now=True)

    def __str__(self):
        return self.postcode


# Create your models here.
class Adres(models.Model):
    class Meta:
        verbose_name_plural = 'Adressen'
        ordering = ['-compleet', 'postcode', 'huisnummer']

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
    )
    slug = models.CharField(
        max_length=36,
        unique=True,
        default=uuid.uuid4,
    )
    vernomen_bewoners = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
    vernomen_adres = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
    postcode = models.ForeignKey(
        Postcode,
        on_delete=models.SET_NULL,
        null=True,
    )
    huisnummer = models.PositiveSmallIntegerField(default=0)
    toevoeging = models.CharField(
        max_length=6,
        blank=True,
        default='',
    )
    in_de_wijk = models.NullBooleanField()
    compleet = models.BooleanField(default=0)
    google_maps_image = models.ImageField(
        blank=True,
        upload_to='images/external_api_cache/google_maps/',
        default='',
    )
    google_streetview_image = models.ImageField(
        blank=True,
        upload_to='images/external_api_cache/google_streetview/',
        default='',
    )
    wijzigings_datum = models.DateField('Laatst gewijzigd', auto_now=True)

    def bewoners(self):
        if self.vernomen_bewoners is '':
            return 'Bewoners Onbekend'
        else:
            return self.vernomen_bewoners

    def bewoond(self):
        if self.bewoners is 'Bewoners Onbekend':
            return False
        else:
            return True

    def straatnaam(self):
        return self.postcode.straatnaam

    def plaatsnaam(self):
        return self.postcode.plaatsnaam

    def deelgemeente(self):
        return self.postcode.deelgemeente

    def provincie(self):
        return self.postcode.provincie

    def volledig_adres(self):
        if self.compleet:
            volledig_adres = '%s %s%s, %s %s' % (
                self.postcode.straatnaam,
                self.huisnummer,
                self.toevoeging,
                self.postcode.postcode,
                self.postcode.plaatsnaam,
            )
        elif self.vernomen_adres:
            volledig_adres = self.vernomen_adres + ', Leerdam'
        else:
            volledig_adres = 'Adres Onbekend'
        return volledig_adres

    def adres_urlformat(self):
        return self.volledig_adres().replace(' ', '%20')

    def get_static_url(self):
        if self.locatie_foto:
            return self.locatie_foto.url
        else:
            return 'images/placeholders/128x128.png'

    def google_streetview_image_url(self):
        return 'https://maps.googleapis.com/maps/api/streetview?size=640x320&location=%s&key=%s' % (
            self.adres_urlformat(),
            settings.GOOGLE_STREETVIEW_IMAGE_KEY,
        )

    def google_maps_image_url(self):
        return 'https://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=17&size=640x320&scale=2&markers=color:green|%s&maptype=hybrid&key=%s' % (
            self.adres_urlformat(),
            self.adres_urlformat(),
            settings.GOOGLE_MAPS_IMAGE_KEY,
        )

    def google_streetview_image_html(self):
        return mark_safe(
            '<img id="streetview-image" src="{url}" width="640" height="320" class="lazyload" />'.format(
                url=self.google_streetview_image_url()
            )
        )

    def google_maps_image_html(self):
        return mark_safe(
            '<img id="static-map-image" src="{url}" width="640" height="320" class="lazyload" />'.format(
                url=self.google_maps_image_url()
            )
        )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('adresboek:adres_details', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        # Check compleet on Save and change appropriately
        if self.postcode.postcode == '0000AA' or self.huisnummer is 0:
            self.compleet = False
        elif self.postcode.postcode is not '0000AA':
            self.compleet = True

        # Create UUID for UUID-les Incomplete Adresses
        if len(str(self.slug)) <= 5 and self.compleet is False:
            self.slug = str(uuid.uuid4())
        # Create Address Slug and Images for Complete Adresses
        elif self.compleet is True:
            # Create Slug
            slug = '%s%s%s' % (
                self.postcode.postcode,
                self.huisnummer,
                self.toevoeging,
            )
            self.slug = slug.replace('None', '')
        super(Adres, self).save(*args, **kwargs)

    def __str__(self):
        return self.volledig_adres()
