from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year_released = models.IntegerField()
    image = models.ImageField(upload_to='movie_images/')
    director = models.CharField(max_length=255)
    description=models.TextField(max_length=255, default="")

    def __str__(self):
        return self.title
