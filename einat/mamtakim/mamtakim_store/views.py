from django.shortcuts import render

# Create your views here.
from django.http import Http404

from .models import Mamtak

def home(request):
    mamtakim = Mamtak.objects.all()
    return render(request, 'home.html', {
        'mamtakim': mamtakim,
    })

def mamtak_detail(request, mamtak_id):
    try:
        mamtak = Mamtak.objects.get(id=mamtak_id)
    except Mamtak.DoesNotExist:
        raise Http404('Mamtak not found')
    return render(request, 'mamtak_detail.html', {
        'mamtak': mamtak,
    })