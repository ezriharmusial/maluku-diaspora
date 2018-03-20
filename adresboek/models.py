from django.db import models
import uuid

# Create your models here.
class Postcode(models.Model):
    class Meta:
        ordering = ["postcode"]

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

    postcode = models.CharField(max_length=6)
    straatnaam = models.CharField(max_length=100)
    plaatsnaam = models.CharField(max_length=100)
    deelgemeente = models.CharField(max_length=100)
    provincie = models.CharField(
        max_length=2, choices=PROVINCIES
    )
    wijzigings_datum = models.DateField(auto_now=True)

    def __str__(self):
        return self.postcode


# Create your models here.
class Adres(models.Model):

    class Meta:
        verbose_name_plural = "Adressen"

    slug = models.CharField(max_length=150, unique=True, default=uuid.uuid4)
    vernomen_bewoners = models.CharField(max_length=100, blank=True, default='')
    vernomen_adres = models.CharField(max_length=100, blank=True, default='')
    postcode = models.ForeignKey(
        Postcode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    huisnummer = models.PositiveSmallIntegerField(default=0)
    toevoeging = models.CharField(max_length=6, null=True, blank=True)
    in_de_wijk = models.NullBooleanField()
    locatie_foto = models.ImageField(
        null=True,
        blank=True,
        upload_to="resources/assets/images/locatie_fotos/",
    )
    wijzigings_datum = models.DateField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('adresboek:adres_details', args=[str(self.slug)])

    def static_locatie_foto_url(self):
        if self.locatie_foto:
            return self.locatie_foto.url.replace(
                "resources/assets",
                "/static/adresboek"
            )
        else:
            return "/static/adresboek/images/placeholders/128x128.png"

    def straatnaam(self):
        return self.postcode.straatnaam

    def plaatsnaam(self):
        return self.postcode.plaatsnaam

    def deelgemeente(self):
        return self.postcode.deelgemeente

    def provincie(self):
        return self.postcode.provincie

    def volledig_adres(self):
        "Volledig adres"
        return '%s %s, %s %s' % (
            self.postcode.straatnaam,
            self.huisnummer,
            self.toevoeging,
            self.postcode.postcode,
            self.postcode.plaatsnaam
        )

    def onvolledig(self):
        if self.postcode.postcode is "0000AA" or self.huisnummer is 0:
            return True
        else:
            return False

    def staticmapurl(self):
        "Volledig adres voor google maps"
        adres_url = '%s+%s%s,%s' % (
            self.postcode.straatnaam.replace(" ", "+"),
            self.huisnummer,
            self.toevoeging,
            self.postcode.plaatsnaam.replace(" ", "+")
        )

        return "https://maps.googleapis.com/maps/api/staticmap?center=" + adres_url + "&zoom=17&size=640x320&scale=2&markers=color:green|" + adres_url + "&maptype=hybrid&key=AIzaSyC2HxF85Npit-Xo_qATdinVo0B4cqIVMaQ"

    def save(self, *args, **kwargs):
        if len(self.slug) <= 25:
            logging.debug("internal uuid used")
            self.slug = uuid.uuid4()
        elif self.huisnummer is not 0 and self.postcode.postcode is not "0000AA" and len(self.slug) <= 25:
            logging.debug("internal composite used")
            self.slug = '%s%s%s' % (
                self.postcode.postcode, self.huisnummer, self.toevoeging
            )
        super(Adres, self).save(*args, **kwargs)

    def __str__(self):
        return self.vernomen_bewoners


# class Persoon(models.Model):
#     DHR = 'Dhr.'
#     MEVR = 'Mevr.'
#     FAM = 'Fam.'
#     ONBEKEND = '-'

#     AANHEF = (
#         (DHR, 'Meneer'),
#         (MEVR, 'Mevrouw '),
#         (FAM, 'Familie'),
#         (ONBEKEND, 'Onbekend'),
#     )

#     aanhef = models.CharField(
#         max_length=2,
#         choices=AANHEF,
#         default=ONBEKEND
#     )
#     voornaam = models.CharField(max_length=50)
#     achternaam = models.CharField(max_length=50)

#     def __str__(self):
#         return self.aanhef + self.postcode
