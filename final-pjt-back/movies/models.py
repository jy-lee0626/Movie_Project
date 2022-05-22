from django.db import models
from django.conf import settings

# class Genre(models.Model):
#     name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now=False, null=True)
    poster_path = models.TextField(null=True)
    overview = models.TextField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    popularity = models.FloatField(null=True)
    # related_name 굳이 만들 필요 없을 것 같아서 안만들었음
    # genres = models.ManyToManyField(Genre)
    genres = models.CharField(max_length=100, null=True)
    # genres_string = models.CharField(max_length=100, null=True)
    movie_id = models.IntegerField(null=True)

class MovieComment(models.Model):
    # 명세에 평점 등록, 수정, 삭제가 있어서 created_at, updated_at 추가함 ->erd에 반영해야함
    movie_id = models.IntegerField(null=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 0.5점 단위로 평점매기면 어떨까 싶어서 IntegerField -> FloatField로 변경, 협의 후 erd 반영
    rank = models.FloatField()
    # comment가 댓글형식으로 달릴텐데 길이 조절이 필요할 것 같아서 TextField -> CharField(max_length=300)으로 변경, 협의 필요
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)