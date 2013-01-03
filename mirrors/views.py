from django.shortcuts import render_to_response
from django.template import RequestContext
from mirrors.models import RsyncMirrors, DistfilesMirrors

def index(request):
    rsyncmirrors = RsyncMirrors.objects.all()
    distfilesmirrors = DistfilesMirrors.objects.all()
    return render_to_response('index.html', {
        'rsyncmirrors': rsyncmirrors,
        'distfilesmirrors': distfilesmirrors,
    }, context_instance=RequestContext(request))

def contacts(request):
    return render_to_response('contacts.html',{},
                              context_instance=RequestContext(request))
