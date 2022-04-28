# Generated by Django 4.0.4 on 2022-04-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_musician_profile_img_alter_musician_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_img',
            field=models.ImageField(blank=True, upload_to='static/album_covers'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='static/profile_images'),
        ),
    ]
