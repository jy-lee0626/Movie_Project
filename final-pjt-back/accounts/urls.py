from django.urls import path
from . import views
from rest_framework_jwt import obtain_jwt_token
# json web token

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/', obtain_jwt_token, name='token'),
    path('profile/', views.profile, name='profile'),
]