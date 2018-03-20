# Generated by Django 2.0.3 on 2018-03-14 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('huisnummer', models.PositiveSmallIntegerField(null=True)),
                ('vernomen_bewoners', models.CharField(blank=True, max_length=100)),
                ('wijzigings_datum', models.DateField(auto_now=True)),
                ('bevestigd', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Adressen',
            },
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=6)),
                ('straatnaam', models.CharField(max_length=100)),
                ('plaatsnaam', models.CharField(max_length=100)),
                ('deelgemeente', models.CharField(max_length=100)),
                ('provincie', models.CharField(choices=[('DR', 'Drenthe'), ('FL', 'Flevoland'), ('FR', 'Friesland'), ('GE', 'Gelderland'), ('GR', 'Groningen'), ('LI', 'Limburg'), ('NB', 'Noord-Brabant'), ('NH', 'Noord-Holland'), ('OV', 'Overijssel'), ('UT', 'Utrecht'), ('ZE', 'Zeeland'), ('ZH', 'Zuid-Holland')], max_length=2)),
                ('breedtegraad', models.DecimalField(blank=True, decimal_places=13, max_digits=15)),
                ('lengtegraad', models.DecimalField(blank=True, decimal_places=13, max_digits=16)),
                ('wijzigings_datum', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['postcode'],
            },
        ),
        migrations.AddField(
            model_name='adres',
            name='postcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adresboek.Postcode'),
        ),
    ]
