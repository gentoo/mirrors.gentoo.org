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
    providerform = None
    contactform = None
    rsyncmirrorform = None
    distfilesmirrorform = None
    if request.method == 'POST':
        providerform = ProviderForm(request.POST)
        contactform = ContactForm(request.POST)
        rsyncmirrorform = RsyncMirrorForm(request.POST)
        distfilesmirrorform = DistfilesMirrorForm(request.POST)
        if providerform.is_valid():
            pass
        if contactform.is_valid():
            pass
        if rsyncmirrorform.is_valid():
            pass
        if distfilesmirrorform.is_valid():
            pass
    else:
        providerform = ProviderForm()
        contactform = ContactForm()
        rsyncmirrorform = RsyncMirrorForm()
        distfilesmirrorform = DistfilesMirrorForm()
    return render_to_response('settings.html', {
        'providerform': providerform,
        'contactform': contactform,
        'rsyncmirrorform': rsyncmirrorform,
        'distfilesmirrorform': distfilesmirrorform,
    }, context_instance = RequestContext(request))
