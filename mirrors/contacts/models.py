from django.db import models

class Continents(models.Model):
    name = models.CharField(max_length=15)

class Countries(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    continent = models.ForeignKey(Continents)

class ContactEmail(models.Model):
    email = models.EmailField()
    bugzilla = models.BooleanField(default=False)

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.ForeignKey(ContactEmail)
    url = models.URLField(null=True)

class Companies(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    url = models.URLField(null=True)

class MirrorAlias(models.Model):
    alias = models.URLField()

class MirrorBugs(models.Model):
    number = models.IntegerField()

class MirrorURL(models.Model):
    STATE_CHOICES = (
        ('working', 'working'),
        ('lagging', 'lagging'),
        ('down', 'down'),
    )
    url = models.URLField()
    alias = models.ForeignKey(MirrorAlias, null=True)
    ipv4 = models.BooleanField(default=True)
    ipv6 = models.BooleanField(default=False)
    state = models.CharField(max_length=10,
        choices=STATE_CHOICES,
        default='working')

class Mirrors(models.Model):
    bugs = models.ManyToManyField(MirrorBugs, null=True)
    country = models.ForeignKey(Countries)
    contacts = models.ManyToManyField(Contacts, null=True)
    company = models.ForeignKey(Companies, null=True)

    class Meta:
        abstract = True

class RsyncMirrors(Mirrors):
    url = models.OneToOneField(MirrorURL)

class DistfilesMirrors(Mirrors):
    http = models.OneToOneField(MirrorURL, null=True, related_name='http')
    ftp = models.OneToOneField(MirrorURL, null=True, related_name='ftp')
    rsync = models.OneToOneField(MirrorURL, null=True, related_name='rsync')
