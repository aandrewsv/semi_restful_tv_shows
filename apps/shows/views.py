from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'newshow.html')

def newshow(request):
    Show.objects.create(
    title=f"{request.POST['title']}",
    network=f"{request.POST['network']}",
    release_date=f"{request.POST['release_date']}", 
    description=f"{request.POST['description']}")
    return redirect('/shows')

def displayshow(request, idn):
    context = {
        'this_show': Show.objects.get(id=idn)
    }
    return render(request, 'displayshow.html', context)

def editshow(request, idn):
    context = {
        'this_show': Show.objects.get(id=idn)
    }
    return render(request, 'editshow.html', context)

def update(request, idn):
    this_show = Show.objects.get(id=idn)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.release_date = request.POST['release_date']
    this_show.description = request.POST['description']
    this_show.save()
    return redirect(f'/shows/{idn}')

def destroy(request, idn):
    this_show = Show.objects.get(id=idn)
    this_show.delete()
    return redirect('/shows')