from django.urls import path

from .views import ( index, login, register, musicians, albums, view_musician, view_album,
create_album, create_musician, logout )


urlpatterns = [
    path('', index),
    path('login/', login),
    path('register/', register),
    path('musicians/', musicians),
    path('create_musician', create_musician),
    path('albums/', albums),
    path('musicians/<int:musician_id>/', view_musician),
    path('albums/<int:album_id>/', view_album),
    path('create_album/', create_album),
    path('logout/', logout),
]




