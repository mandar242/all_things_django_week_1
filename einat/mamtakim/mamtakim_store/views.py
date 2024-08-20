from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from mamtakim_store.models import Mamtak
from mamtakim_store.forms import MamtakForm

'''
#basic response
def home(request):
    return HttpResponse('<p> Home view</p>')
'''
# Create your views here.

def home(request):
    mamtakim = Mamtak.objects.all() #mamtakim contains a full list of all objects
    return render(request, 'home.html', {
        'mamtakim': mamtakim,
    })
'''SOME NOTES:
When using the render function, you need to start working with Templates.
Render function 
first argument = request argument that's passed onto the view
second argument = name of template we'd like to use
third = dictionary with information we want to use inside the template. The keys inside the dictionary are used as variables for the template we are calling

'''

def mamtak_detail(request, mamtak_id):
    try:
        mamtak = Mamtak.objects.get(id=mamtak_id)
    except Mamtak.DoesNotExist:
        raise Http404('Mamtak not found')
    return render(request, 'mamtak_detail.html', {
        'mamtak': mamtak,
    })

def mamtak_delete(request, mamtak_id):
    if 'delete' in request.POST:
            pk = request.POST.get('delete')
            mamtak = Mamtak.objects.get(id=mamtak_id)
            mamtak.delete()
    return render(request, 'mamtak_detail.html', {
        'mamtak': mamtak,
    })

def index(request):
    context = {}
    form = MamtakForm()
    mamtakim = Mamtak.objects.all()
    context['mamtakim'] = mamtakim
    context['title'] = 'Home'
 
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = MamtakForm(request.POST)
            else:
                mamtak = Mamtak.objects.get(id=pk)
                form = MamtakForm(request.POST, instance=mamtak)
            form.save()
            form = MamtakForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            mamtak = Mamtak.objects.get(id=pk)
            mamtak.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            mamtak = Mamtak.objects.get(id=pk)
            form = MamtakForm(instance=mamtak)

    context['form'] = form
    return render(request, 'home2.html', context)
