from django.forms.models import modelformset_factory
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
            try:
                form.save()
                return HttpResponseRedirect('/settings/')
            except:
                raise
    else:
        form = ProviderForm()
    return render_to_response('settings_add_provider.html', {
        'form': form,
    }, context_instance = RequestContext(request))

def settings_add_contact(request):
    ContactEmailFormSet = modelformset_factory(ContactEmail, extra=5)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            formset = ContactEmailFormSet(
                request.POST,
                queryset=ContactEmail.objects.none(),
                initial=[{'contact': Contacts.objects.get(name=form.cleaned_data['name'])}]
            )
            if formset.is_valid():
                try:
                    formset.save()
                    return HttpResponseRedirect('/settings/')
                except:
                    raise
            else:
                Contacts.objects.get(name=form.cleaned_data['name']).delete()
    else:
        form = ContactForm()
        formset = ContactEmailFormSet(queryset=ContactEmail.objects.none())
    return render_to_response('settings_add_contact.html', {
        'form': form,
        'formset': formset,
    }, context_instance = RequestContext(request))
