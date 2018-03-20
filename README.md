# Ambon Diaspora

Ambon Diaspora Web Experiment is een initiatief van de Amboneese gemeenschap in Leerdam om het verleden en de toekomst in het nu te verbinden, met behulp van ICT technologie. Oude culturele tradities en communicatie structuren verdwijnen door gelijdelijke assimilatie in de heersende culturen van de landen van onze ballingschap. Ambon diaspora is een middel om opnieuw gehoor te geven aan het belang van het gebruik van deze oude tradities en structuren. Structuren en tradities die niet zonder reden al 1000en jaren de basis vormen van ons bestaan.

## Benodigdheden
Ambon Diaspora draait zelfstandig in Docker Containers, maar om de boel te bewerken is het aan te raden om eerst de benodigde software te installeren. Instructies over de installatie van deze software pakketen zijn te vinden op de respectievelijke sites.
* Python 3
* Docker 17.12+
* Docker-compose 1.19.0
* Node v8.9.4
* NPM 5.7.1
* Yarn 1.3.2

## Installatie
Na dat de benodigde software aanwezig is, is het tijd om een clone van de repository te maken en de boel op te starten.
<pre>
git clone https://github.com/ezriharmusial/ambon-diaspora.git
cd ambon-diaspora
docker-compose up
</pre>

## Inhoud docker containers
* Python 3
 * Django 2.0
 * djangorestframework
 * django-filter
 * Pillow
 * psycopg2-binary
* PostgreSQL
* PGadmin 4