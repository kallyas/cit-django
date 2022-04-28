import json
from functools import wraps
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MusicianForm, AlbumForm, LoginForm

from .models import Musician, Album


# create login_required decorator
def login_required(function):
    @wraps(function)
    def inner(request, *args, **kwargs):
        if 'username' in request.session:
            return function(request, *args, **kwargs)
        else:
            request.session['next'] = request.path
            return HttpResponseRedirect('/login?next=' + request.path)
    return inner

def login_not_required(function):
    @wraps(function)
    def inner(request, *args, **kwargs):
        if 'username' in request.session:
            return HttpResponseRedirect('/')
        else:
            return function(request, *args, **kwargs)
    return inner

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_not_required
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.user_authenticate(request):
                # create a session and redirect user to homepage
                request.session['username'] = form.cleaned_data['username']
                if 'next' in request.session:
                    return HttpResponseRedirect(request.session['next'])
                else:
                    return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html', { 'login_errors': 'Invalid username or password' })
        else:
            return render(request, 'login.html', { 'errors': form.errors })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

@login_not_required
def register(request):
    return render(request, 'register.html')

@login_required
def musicians(request):
     musicians = Musician.objects.all()
     return render(request, 'musicians.html', {'musicians': musicians})


@login_required
def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})

@login_required
def view_musician(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    return render(request, 'musician.html', {'musician': musician})

@login_required
def view_album(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'album.html', {'album': album})

@login_required
def create_album(request):
    # use the AlbumForm to create a new Album
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            return HttpResponseRedirect('/albums')
        else:
            return render(request, 'create_album.html', { 'errors': form.errors })
    else:
        form = AlbumForm()
        musicians = Musician.objects.all()
    return render(request, 'create_album.html', {'form': form, 'artists': musicians})


@login_required
def create_musician(request):
    # use the MusicianForm to create a new Musician
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            musician = form.save()
            return HttpResponseRedirect('/musicians')
        else:
            return render(request, 'create_musician.html', { 'errors': form.errors })
    else:
        form = MusicianForm()
    return render(request, 'create_musician.html', {'form': form})


@login_required
def logout(request):
    # remove the session and redirect user to homepage
    request.session.flush()
    return HttpResponseRedirect('/')