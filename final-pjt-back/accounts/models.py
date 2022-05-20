from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # https://it-tutorial.tistory.com/146 여기 보고 따라서 작성했음
    GENDER_CHOICES = [
        ('Male', 'male'),
        ('Female', 'female'),
    ]
    
    
    profile_image=models.ImageField(null=True)
    gender = models.CharField(("Gender"), max_length=80, choices=GENDER_CHOICES)
    favorite_movies = models.ManyToManyField("movies.Movie", max_length=5) # 관심 영화를 최대 5개 까지 저정하려면 어떻게 해야할까?
