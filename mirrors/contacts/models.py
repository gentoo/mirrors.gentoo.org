from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email1 = models.EmailField()
    email2 = models.EmailField()
    email3 = models.EmailField()
    email4 = models.EmailField()
    email5 = models.EmailField()
    bugzilla1 = models.BooleanField(default=False)
    bugzilla2 = models.BooleanField(default=False)
    bugzilla3 = models.BooleanField(default=False)
    bugzilla4 = models.BooleanField(default=False)
    bugzilla5 = models.BooleanField(default=False)
    url = models.URLField(blank=True, null=True)

class Mirrors(models.Model):
    url1 = models.URLField()
    url2 = models.URLField()
    ipv4 = models.BooleanField(default=True)
    ipv6 = models.BooleanField(default=False)
    contact = models.ManyToManyField(Contacts)

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
