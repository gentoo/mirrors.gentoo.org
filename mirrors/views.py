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
    FtpUrlForm = modelform_factory(MirrorURL, form=MirrorURLForm)
    HttpUrlForm = modelform_factory(MirrorURL, form=MirrorURLForm)
    RsyncUrlForm = modelform_factory(MirrorURL, form=MirrorURLForm)
    FtpAliasForm = modelform_factory(MirrorAlias, form=MirrorAliasForm)
    HttpAliasForm = modelform_factory(MirrorAlias, form=MirrorAliasForm)
    RsyncAliasForm = modelform_factory(MirrorAlias, form=MirrorAliasForm)
    BugsFormset = modelformset_factory(MirrorBugs, extra=3)
    if request.method == 'POST':
        distfilesmirror_form = DistfilesMirrorForm(request.POST)

        http_url_form = HttpUrlForm(request.POST)
        ftp_url_form = FtpUrlForm(request.POST)
        rsync_url_form = RsyncUrlForm(request.POST)

        http_alias_form = HttpAliasForm(request.POST)
        ftp_alias_form = FtpAliasForm(request.POST)
        rsync_alias_form = RsyncAliasForm(request.POST)

        bugs_formset = BugsFormset(
            request.POST,
            queryset=MirrorBugs.objects.none()
        )
        if http_alias_form.is_valid() and rsync_alias_form.is_valid() and ftp_alias_form.is_valid()\
                and http_url_form.is_valid() and ftp_url_form.is_valid() and rsync_url_form.is_valid():
                ftp_alias = ftp_alias_form.save()
                http_alias = http_alias_form.save()
                rsync_alias = rsync_alias_form.save()

                ftp_url = ftp_url_form.save(commit=False)
                ftp_url.alias = ftp_alias
                ftp_url.save()

                http_url = http_url_form.save(commit=False)
                http_url.alias = http_alias
                http_url.save()

                rsync_url = rsync_url_form.save(commit=False)
                rsync_url.alias = rsync_alias
                rsync_url.save()
                if distfilesmirror_form.is_valid() and bugs_formset.save():
                    try:
                        distfilesmirror = distfilesmirror_form.save(commit=False)
                        distfilesmirror.ftp = ftp_url
                        distfilesmirror.http = http_url
                        distfilesmirror.rsync = rsync_url
                        distfilesmirror.save()
                        bugs_formset.save()
                        return HttpResponseRedirect('/settings/')
                    except:
                        raise
    else:
        distfilesmirror_form = DistfilesMirrorForm()
        http_url_form = HttpUrlForm()
        ftp_url_form = FtpUrlForm()
        rsync_url_form = RsyncUrlForm()
        http_alias_form = HttpAliasForm()
        ftp_alias_form = FtpAliasForm()
        rsync_alias_form = RsyncAliasForm()
        bugs_formset = BugsFormset(queryset=MirrorBugs.objects.none())
    return render_to_response('settings_add_distfilesmirror.html', {
        'distfilesmirror_form': distfilesmirror_form,
        'http_form': http_url_form,
        'http_alias_form': http_alias_form,
        'ftp_form': ftp_url_form,
        'ftp_alias_form': ftp_alias_form,
        'rsync_form': rsync_url_form,
        'rsync_alias_form': rsync_alias_form,
        'bugs_formset': bugs_formset,
    }, context_instance=RequestContext(request))
