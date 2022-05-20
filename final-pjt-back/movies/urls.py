from django.urls import path
from . import views

# app_name = 'movies'

urlpatterns = [
    path('movies/nowplaying', views.now_playing_movie),
    path('movies/popular', views.popular_movie),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    
]