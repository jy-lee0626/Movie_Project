from django.urls import path
from . import views

# app_name = 'movies'

urlpatterns = [
    path('nowplaying/', views.now_playing_movies),
    # path('movies/popular', views.popular_movie),
    path('<int:movie_id>/', views.movie_detail),
    path('my_popular/', views.my_popular_movie),
    path('<int:movie_num>/like/', views.like_movie),
    path('search/<query>/', views.search),
    path('movies/<int:movie_id>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    
]