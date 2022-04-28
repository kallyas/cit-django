from django.contrib import admin

# Register your models here.
from .models import Musician, Album

admin.site.register(Musician)
admin.site.register(Album)
