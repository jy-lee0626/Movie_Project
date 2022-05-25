from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, null=True)
    poster_path = models.TextField(null=True)
    overview = models.TextField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    popularity = models.FloatField(null=True)
    genres = models.CharField(max_length=100, null=True)
    movie_num = models.IntegerField(null=True)
    movie_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    like_count = models.IntegerField(default=0)
    
class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.FloatField()
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)