from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import os


class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0, validators=[
                               MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f"{self.movie.title} - {self.rating}"
