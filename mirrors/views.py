from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from mirrors.models import Providers, RsyncMirrors, DistfilesMirrors
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
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider = Providers(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                url = form.cleaned_data['url'],
            )
            try:
                provider.save()
                return HttpResponseRedirect('/settings/')
            except:
                raise
    else:
        form = ProviderForm()
    return render_to_response('settings_add_provider.html', {
        'form': form,
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
