from django.db import models
from mirrors.choices import *
from international.models import Country

class ContactEmail(models.Model):
    email = models.EmailField()
    bugzilla = models.BooleanField(default=False)

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.ForeignKey(ContactEmail)
    url = models.URLField(null=True, verbose_name='URL')

class Providers(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, unique=True)
    url = models.URLField(null=True, verbose_name='URL', unique=True)

class MirrorAlias(models.Model):
    alias = models.URLField()

class MirrorBugs(models.Model):
    number = models.IntegerField()

class MirrorURL(models.Model):
    url = models.URLField()
    alias = models.ForeignKey(MirrorAlias, null=True)
    ipv4 = models.BooleanField(default=True)
    ipv6 = models.BooleanField(default=False)
    status = models.CharField(max_length=10,
        choices=STATUS_CHOICES,
        default='Working')

class Mirrors(models.Model):
    bugs = models.ManyToManyField(MirrorBugs, null=True)
    country = models.ForeignKey(Country)
    contacts = models.ManyToManyField(Contacts, null=True)
    provider = models.ForeignKey(Providers, null=True)

    class Meta:
        abstract = True

class RsyncMirrors(Mirrors):
    url = models.OneToOneField(MirrorURL, verbose_name='URL')

class DistfilesMirrors(Mirrors):
    http = models.OneToOneField(MirrorURL, null=True, related_name='http', verbose_name='HTTP')
    ftp = models.OneToOneField(MirrorURL, null=True, related_name='ftp', verbose_name='FTP')
    rsync = models.OneToOneField(MirrorURL, null=True, related_name='rsync')
