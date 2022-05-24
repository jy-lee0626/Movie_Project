from django.urls import path
from . import views

# app_name = 'movies'

urlpatterns = [
    path('nowplaying/', views.now_playing_movies),
    # path('movies/popular', views.popular_movie),
    path('<int:movie_num>/', views.movie_detail),
    path('my_popular/', views.my_popular_movie),
    path('<int:movie_num>/like/', views.like_movie),
    path('search/', views.search),
    path('<int:movie_pk>/comments/', views.create_comment),
    # path('comments/', views.comment_list),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail),
    
]