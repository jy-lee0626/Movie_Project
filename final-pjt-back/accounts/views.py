from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)



@api_view(['GET'])
def user_match(request, username):
    user = get_object_or_404(User, username=username)
    all_users = User.objects.all()
    movie_count = 0
    match = None
    for other in all_users:
        if other.pk==user.pk: # gender로 바꿔서 쓸 수도 있음
            continue
        cnt = 0
        for movie in user.like_movies.all():
            if movie.movie_like.filter(pk=other.pk):
                cnt += 1
        if cnt >= movie_count: 
            movie_count = cnt
            match = other
    serializer = ProfileSerializer(match)
    context = {
        'user': serializer.data,
        'count': movie_count, # 좋아요 한 영화가 몇 개 겹치는지 
    }
    return Response(context) 



        
