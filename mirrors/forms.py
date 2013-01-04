from django.forms import ModelForm
from mirrors.models import Contacts, RsyncMirrors, DistfilesMirrors

class ContactForm(ModelForm):
    class Meta:
        model = Contacts

class RsyncMirrorForm(ModelForm):
    class Meta:
        model = RsyncMirrors

class DistfilesMirrorForm(ModelForm):
    class Meta:
        model = DistfilesMirrors

