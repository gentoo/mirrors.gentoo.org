from django.forms.models import modelform_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from mirrors.models import *
from mirrors.forms import *


def index(request):
    portagemirror = PortageMirror.objects.all()
    distfilesmirror = DistfilesMirror.objects.all()
    return render_to_response('index.html', {
        'portagemirror': portagemirror,
        'distfilesmirror': distfilesmirror,
    }, context_instance=RequestContext(request))


def settings(request):
    return render_to_response('settings_general.html', {
    }, context_instance=RequestContext(request))


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
    }, context_instance=RequestContext(request))


def settings_add_contact(request):
    ContactEmailFormSet = modelformset_factory(ContactEmail, extra=5)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        formset = ContactEmailFormSet(
            request.POST,
            queryset=ContactEmail.objects.none()
        )
        if form.is_valid():
            form.save()
            '''
            Copy request.POST to make it mutable, and add in the newly created
            'data' QueryDict the table ID of the newly created contact
            '''
            form_contact = Contacts.objects.get(
                name=form.cleaned_data['name']).id
            data = request.POST.copy()
            for i in range(5):
                if data['form-%s-email' % i]:
                    data.update({'form-%s-contact' % i: form_contact})
            formset = ContactEmailFormSet(
                data, queryset=ContactEmail.objects.none())
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
    }, context_instance=RequestContext(request))


def settings_add_portagemirror(request):
    UrlForm = modelform_factory(MirrorURL, form=MirrorURLForm)
    AliasForm = modelform_factory(MirrorAlias, form=MirrorAliasForm)
    BugsFormset = modelformset_factory(MirrorBugs, extra=3)
    if request.method == 'POST':
        portagemirror_form = PortageMirrorForm(request.POST)
        url_form = UrlForm(request.POST)
        alias_form = AliasForm(request.POST)
        bugs_formset = BugsFormset(
            request.POST,
            queryset=MirrorBugs.objects.none()
        )
        if alias_form.is_valid()and url_form.is_valid():
            alias = alias_form.save()
            url = url_form.save(commit=False)
            url.alias = alias
            url.save()
            if portagemirror_form.is_valid() and bugs_formset.save():
                try:
                    portagemirror = portagemirror_form.save(commit=False)
                    portagemirror.url = url
                    portagemirror.save()
                    bugs_formset.save()
                    return HttpResponseRedirect('/settings/')
                except:
                    raise
    else:
        portagemirror_form = PortageMirrorForm()
        url_form = UrlForm()
        alias_form = AliasForm()
        bugs_formset = BugsFormset(queryset=MirrorBugs.objects.none())
    return render_to_response('settings_add_portagemirror.html', {
        'portagemirror_form': portagemirror_form,
        'url_form': url_form,
        'alias_form': alias_form,
        'bugs_formset': bugs_formset,
    }, context_instance=RequestContext(request))


def settings_add_distfilesmirror(request):
    UrlForm = modelform_factory(MirrorURL, form=MirrorURLForm)
    AliasForm = modelform_factory(MirrorAlias, form=MirrorAliasForm)
    BugsFormset = modelformset_factory(MirrorBugs, extra=3)
    if request.method == 'POST':
        distfilesmirror_form = DistfilesMirrorForm(request.POST)
        url_form = UrlForm(request.POST)
        alias_form = AliasForm(request.POST)
        bugs_formset = BugsFormset(
            request.POST,
            queryset=MirrorBugs.objects.none()
        )
        if alias_form.is_valid() and url_form.is_valid():
                alias = alias_form.save()

                distfiles_url = url_form.save(commit=False)
                distfiles_url.alias = alias
                distfiles_url.save()

                if distfilesmirror_form.is_valid() and bugs_formset.save():
                    try:
                        distfilesmirror = distfilesmirror_form.save(commit=False)
                        distfilesmirror.url = distfiles_url
                        distfilesmirror.save()
                        bugs_formset.save()
                        return HttpResponseRedirect('/settings/')
                    except:
                        raise
    else:
        distfilesmirror_form = DistfilesMirrorForm()
        url_form = UrlForm()
        alias_form = AliasForm()
        bugs_formset = BugsFormset(queryset=MirrorBugs.objects.none())
    return render_to_response('settings_add_distfilesmirror.html', {
        'distfilesmirror_form': distfilesmirror_form,
        'url_form': url_form,
        'alias_form': alias_form,
        'bugs_formset': bugs_formset,
    }, context_instance=RequestContext(request))
