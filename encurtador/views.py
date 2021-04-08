from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
import uuid

# Create your views here.
def index(request):
    return render (request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        nova_url = Url(link=link, uuid=uid)
        nova_url.save()
        return HttpResponse(uid)

def go(request, pk):
    detalhes_url = Url.objects.get(uuid=pk)
    return redirect(detalhes_url.link)
    
