from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='static/profile_images', blank=True)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'instrument': self.instrument,
            'profile_img': self.profile_img.url
        }

    def get_img_url(self):
        return self.profile_img.url if self.profile_img else '/static/profile_images/default.jpg'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return '/musicians/' + str(self.id) + '/'



class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    cover_img = models.ImageField(upload_to='static/album_covers', blank=True)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'artist': self.artist.to_dict(),
            'name': self.name,
            'release_date': self.release_date,
            'cover_img': self.cover_img.url,
            'num_stars': self.num_stars
        }

    def get_absolute_url(self):
        return '/albums/' + str(self.id) + '/'

    def get_img_url(self):
        return self.cover_img.url

    def get_artist_url(self):
        return '/musicians/' + str(self.artist.id) + '/'

    # get number of albums in the database
    def get_num_albums(self):
        return Album.objects.count()

    def render_width(self):
        # render width such that the output is 0, for first album, 33% for second, 66% for third, and start again 0 for fourth, 33% fifth, 66% for sixth, etc.
        width = ['0%', '33%', '66%']
        percent = ''
        if self.id % 3 == 0:
            percent = width[0]
        elif self.id % 3 == 1:
            percent = width[1]
        else:
            percent = width[2]

        style = "position: absolute; left: {}; top: 0px".format(percent)
        return style

