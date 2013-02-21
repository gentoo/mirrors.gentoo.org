from django.db import models
from mirrors.choices import *
from international.models import Country


class Contacts(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(blank=True, verbose_name='URL')

    def __unicode__(self):
        return self.name

class ContactEmail(models.Model):
    contact = models.ForeignKey(Contacts)
    email = models.EmailField(unique=True)
    bugzilla = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email

class Providers(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True, verbose_name='URL')

    def __unicode__(self):
        return self.name

class MirrorAlias(models.Model):
    alias = models.URLField()

class MirrorBugs(models.Model):
    number = models.IntegerField(blank=True, verbose_name="Mirror Bug")

class MirrorURL(models.Model):
    url = models.URLField(verbose_name="URL")
    alias = models.ForeignKey(MirrorAlias, null=True)
    ipv4 = models.BooleanField(default=True, verbose_name="IPv4")
    ipv6 = models.BooleanField(default=False, verbose_name="IPv6")
    status = models.CharField(max_length=10,
        choices=STATUS_CHOICES,
        default='Working')

class Mirror(models.Model):
    bugs = models.ManyToManyField(MirrorBugs, null=True)
    country = models.ForeignKey(Country)
    contacts = models.ManyToManyField(Contacts, null=True)
    provider = models.ForeignKey(Providers, null=True)

    class Meta:
        abstract = True

class PortageMirror(Mirror):
    url = models.ForeignKey(MirrorURL, unique=True)

class DistfilesMirror(Mirror):
    http = models.ForeignKey(MirrorURL, null=True, unique=True, related_name='http', verbose_name='HTTP')
    ftp = models.ForeignKey(MirrorURL, null=True, unique=True, related_name='ftp', verbose_name='FTP')
    rsync = models.ForeignKey(MirrorURL, null=True, unique=True, related_name='rsync')
