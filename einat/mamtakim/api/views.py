from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import Http404
from mamtakim_store.models import Mamtak
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Mamtak.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


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
