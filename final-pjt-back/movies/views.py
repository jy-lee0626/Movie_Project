import requests
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre, MovieComment
from rest_framework import serializers, status
from .serializer import *
from django.shortcuts import get_list_or_404, get_object_or_404


# 현재상영중인영화리스트
# 인기영화리스트
# 영화검색결과
# 영화상세정보
# 영화코멘트

@api_view(['GET'])
def now_playing_movie(request):
    if request.method == 'GET':
        results = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=03f03c44041dd5b89d9605ef7395f631&language=en-US&page=1')
        results = results.json().get('results')
        now_movie = Movie(title=results.get('title'), overview=results.get('overview'), release_date=results.get('release_date'), poster_path=results.get('poster_path'),genres=results.get('genre_ids'), vote_average=results.get('vote_average'), vote_count=results.get('vote_count'), movie_id=results.get('id'))
        now_movie.save()
    return Response(status=status.HTTP_201_CREATED)



@api_view(['GET'])
def popular_movie(request):
    if request.method == 'GET':
        results = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=03f03c44041dd5b89d9605ef7395f631&language=en-US&page=1')
        results = results.json().get('results')
        popular = Movie(title=results.get('title'), overview=results.get('overview'), release_date=results.get('release_date'), poster_path=results.get('poster_path'),genres=results.get('genre_ids'), vote_average=results.get('vote_average'), vote_count=results.get('vote_count'), movie_id=results.get('id'))
        popular.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_search(request):
    if request.method == 'GET':
        results = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=03f03c44041dd5b89d9605ef7395f631&language=en-US&query={title(string)}&page=1&include_adult=false')
        results = results.json().get('results')
        search = Movie(title=results.get('title'), overview=results.get('overview'), release_date=results.get('release_date'), poster_path=results.get('poster_path'),genres=results.get('genre_ids'), vote_average=results.get('vote_average'), vote_count=results.get('vote_count'), movie_id=results.get('id'))
        search.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail(request):
    if request.method == 'GET':
        results = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=03f03c44041dd5b89d9605ef7395f631&language=en-US')
        results = results.json().get('results')
        search = Movie(title=results.get('title'), overview=results.get('overview'), release_date=results.get('release_date'), poster_path=results.get('poster_path'),genres=results.get('genre_ids'), vote_average=results.get('vote_average'), vote_count=results.get('vote_count'), movie_id=results.get('id'))
        search.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(MovieComment)
    serializer = MovieCommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(MovieComment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = MovieCommentSerializer(comment)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'데이터 {comment_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieCommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
