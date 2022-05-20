import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre, MovieComment
from rest_framework import serializers, status
from .serializers import *
from django.http import JsonResponse




@api_view(['GET'])
def now_playing_movies(request):
    if request.method == 'GET':
        if Movie.objects.exists():
            movie = get_list_or_404(Movie)
            serializer = MovieListSerializer(movie, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            results = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&page=1')
            results = results.json().get('results')
            for result in results:
                now_movie = Movie(title=result.get('title'), overview=result.get('overview'), release_date=result.get('release_date'), poster_path=result.get('poster_path'),genres=result.get('genre_ids'), vote_average=result.get('vote_average'), vote_count=result.get('vote_count'), movie_id=result.get('id'))
                if not Movie.objects.filter(title=now_movie.title):
                    now_movie.save()
            movie = get_list_or_404(Movie)
            serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)





# client에서 영화 id 보내주면 해당하는 영화의 detail정보 db에 저장 안하고 json파일 반환
@api_view(['GET'])
def movie_detail(request, movie_id):
    if request.method == 'GET':
        result = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR')
        result = result.json()
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)





# 영화검색결과
@api_view(['GET'])
def search(request, query):
    if request.method == 'GET':
        result = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&query={query}&page=1&include_adult=false')
        result = result.json().get('results')
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)





# ----------------------------------------------------------------





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
def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
