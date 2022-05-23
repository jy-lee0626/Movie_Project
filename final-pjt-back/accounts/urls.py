from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profile/<username>/user_match/', views.user_match),
]
