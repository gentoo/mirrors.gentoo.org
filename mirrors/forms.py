from django.forms import ModelForm
from django import forms
from mirrors.models import MirrorAlias, MirrorBugs, MirrorURL, Providers, Contacts, ContactEmail, PortageMirror, DistfilesMirror

class ProviderForm(ModelForm):
    class Meta:
        model = Providers

class ContactEmailForm(ModelForm):
    class Meta:
        model = ContactEmail

class ContactForm(ModelForm):
    class Meta:
        model = Contacts

class MirrorAliasForm(ModelForm):
    class Meta:
        model = MirrorAlias

class MirrorBugsForm(ModelForm):
    class Meta:
        model = MirrorBugs

class MirrorURLForm(ModelForm):
    class Meta:
        model = MirrorURL
        exclude = ('alias',)

class PortageMirrorForm(ModelForm):
    class Meta:
        model = PortageMirror
        exclude = ('bugs','url',)

class DistfilesMirrorForm(ModelForm):
    class Meta:
        model = DistfilesMirror
