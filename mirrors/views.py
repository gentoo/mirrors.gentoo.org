from django.shortcuts import render_to_response
from django.template import RequestContext
from mirrors.models import RsyncMirrors, DistfilesMirrors


def index(request):
    rsyncmirror = RsyncMirrors.objects.all()
    distmirror = DistfilesMirrors.objects.all()
    return render_to_response('index.html', {'rsyncmirror': rsyncmirror, 'distmirror': distmirror}, context_instance=RequestContext(request))
