# Generated by Django 5.0.2 on 2024-03-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rating_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images'),
        ),
    ]
