from django.forms import ModelForm
from mirrors.models import Providers, Contacts, RsyncMirrors, DistfilesMirrors

class ProviderForm(ModelForm):
    class Meta:
        model = Providers

class ContactForm(ModelForm):
    class Meta:
        model = Contacts

class RsyncMirrorForm(ModelForm):
    class Meta:
        model = RsyncMirrors

class DistfilesMirrorForm(ModelForm):
    class Meta:
        model = DistfilesMirrors

