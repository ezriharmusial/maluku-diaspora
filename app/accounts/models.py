from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profiel(models.Model):
    GEMEENSCHAP = 1
    DERDEN = 2
    ROLLEN = (
        (GEMEENSCHAP, 'Deel van de Gemeenschap'),
        (DERDEN, 'Derden'),
    )
    gebruiker = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    geboortedatum = models.DateField(
        null=True,
        blank=True,
    )
    rol = models.PositiveSmallIntegerField(
        choices=ROLLEN,
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to='images/avatars/',
        null=True,
        blank=True,
    )

    def __str__(self):  # __unicode__ for Python 2
        return self.gebruiker.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profiel(gebruiker=instance)
    instance.profiel.save()


def get_full_name(self):
    '''
    Returns the first_name plus the last_name, with a space in between.
    '''
    full_name = '%s %s' % (User.first_name, User.last_name)
    return full_name.strip()


def get_short_name(self):
    '''
    Returns the short name for the user.
    '''
    return User.first_name


def get_email(self):
    '''
    Returns the short Email of the user.
    '''
    return User.email


def static_avatar_url(self):
    if self.avatar:
        return self.avatar
    else:
        return 'images/placeholders/128x128.png'
