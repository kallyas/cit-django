from django import forms

from .utils import generate_random_reviews

from .models import Musician, Album
from django.contrib.auth import authenticate, login


class MusicianForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    instrument = forms.CharField(label='Instrument', max_length=100)
    profile_img = forms.ImageField(label='Profile Image')


    def save(self):
        musician = Musician.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            instrument=self.cleaned_data['instrument'],
            profile_img=self.cleaned_data['profile_img']
        )
        return musician


class AlbumForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    artist = forms.CharField(label='Artist', max_length=100)
    release_date = forms.DateField(label='Release Date')
    cover_img = forms.ImageField(label='Cover Image')


    def save(self):
        album = Album.objects.create(
            name=self.cleaned_data['name'],
            artist = Musician.objects.get(id=self.cleaned_data['artist']),
            release_date=self.cleaned_data['release_date'],
            cover_img=self.cleaned_data['cover_img'],
            num_stars=generate_random_reviews()
        )
        return album


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

    def user_authenticate(self, request):
        username = self.cleaned_data['username']
        password=self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
