from django.shortcuts import render_to_response
from django.template import RequestContext
from mirrors.models import RsyncMirrors, DistfilesMirrors
from mirrors.forms import *

def index(request):
    rsyncmirrors = RsyncMirrors.objects.all()
    distfilesmirrors = DistfilesMirrors.objects.all()
    return render_to_response('index.html', {
        'rsyncmirrors': rsyncmirrors,
        'distfilesmirrors': distfilesmirrors,
    }, context_instance=RequestContext(request))

def settings(request):
    return render_to_response('settings.html', {
    }, context_instance = RequestContext(request))

def settings_add_provider(request):
    providerform = None
    if request.method == 'POST':
        providerform = ProviderForm(request.POST)
        if providerform.is_valid():
            pass
    else:
        providerform = ProviderForm()
    print request.POST
    return render_to_response('settings_add_provider.html', {
        'providerform': providerform,
    }, context_instance = RequestContext(request))

def settings_add_contact(request):
    contactform = None
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            pass
    else:
        contactform = ContactForm()
    return render_to_response('settings_add_contact.html', {
        'contactform': contactform,
    }, context_instance = RequestContext(request))
