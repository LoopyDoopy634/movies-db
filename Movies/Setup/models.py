from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year_released = models.IntegerField()
    image = models.ImageField(upload_to='movie_images/')
    director = models.CharField(max_length=255)
    description=models.TextField(max_length=255, default="")

    def __str__(self):
        return self.title
    
class UserReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.username} - {self.rating}"
