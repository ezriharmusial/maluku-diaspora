# Generated by Django 2.0.3 on 2018-03-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresboek', '0014_auto_20180319_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='vernomen_adres',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='adres',
            name='vernomen_bewoners',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
