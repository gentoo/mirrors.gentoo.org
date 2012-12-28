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

class MirrorAlias(models.Model):
    alias = models.URLField()

class MirrorBugs(models.Model):
    number = models.IntegerField()

class Mirrors(models.Model):
    STATE_CHOICES = (
        ('working', 'working'),
        ('lagging', 'lagging'),
        ('down', 'down'),
    )
    url = models.URLField()
    alias = models.ForeignKey(MirrorAlias, null=True)
    ipv4 = models.BooleanField(default=True)
    ipv6 = models.BooleanField(default=False)
    bugs = models.ManyToManyField(MirrorBugs, null=True)
    country = models.ForeignKey(Countries)
    contacts = models.ManyToManyField(Contacts, null=True)
    state = models.CharField(max_length=10,
        choices=STATE_CHOICES,
        default='working')

    class Meta:
        abstract = True

class RsyncMirrors(Mirrors):
    pass

class DistfilesMirrors(Mirrors):
    PROTOCOL_CHOICES = (
        ('http', 'http'),
        ('ftp', 'ftp'),
        ('rsync', 'rsync'),
    )
    protocol = models.CharField(max_length=5,
        choices=PROTOCOL_CHOICES,
        default='http')
