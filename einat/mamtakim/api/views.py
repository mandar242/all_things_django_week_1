from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import Http404
from mamtakim_store.models import Mamtak
from .serializers import MamtakSerializer

@api_view(['GET'])
def getData(request):
    items = Mamtak.objects.all()
    serializer = MamtakSerializer(items, many=True)
    return Response(serializer.data) #passing information to Response will be returned as json data

@api_view(['POST'])
def addMamtak(request):
    serializer = MamtakSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def mamtak_detail(request, mamtak_id):
    try:
        mamtak = Mamtak.objects.get(id=mamtak_id)
    except Mamtak.DoesNotExist:
        raise Http404('Mamtak not found')
    return render(request, 'mamtak_detail.html', {
        'mamtak': mamtak,
    })