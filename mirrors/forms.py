from django.forms import ModelForm
from django import forms
from mirrors.models import Providers, Contacts, ContactEmail, RsyncMirrors, DistfilesMirrors

class ProviderForm(ModelForm):
    class Meta:
        model = Providers

class ContactEmailForm(ModelForm):
    class Meta:
        model = ContactEmail

class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        exclude = ['email']

class RsyncMirrorForm(ModelForm):
    class Meta:
        model = RsyncMirrors

class DistfilesMirrorForm(ModelForm):
    class Meta:
        model = DistfilesMirrors
