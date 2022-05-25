from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Review, Comment
from movies.models import Movie
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET', 'POST'])
def reviews(request): 
    if request.method == 'GET':
        all_reviews = Review.objects.order_by('-created_at')
        serializer = ReviewListSerializer(all_reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        title = request.data.get('title')
        content = request.data.get('content')
        review = Review(title=title,content=content, user=request.user)
        review.save()
        serializer = ReviewSerializer(review)
        print(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            data = {
                'delete': f'{review_pk}번 글이 성공적으로 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT) 
    # title. content, movie 수정 가능 
    elif request.method == 'PUT':
        review.title = request.data.get('title')
        review.content = request.data.get('content')
        print(request.data)
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)



@api_view(['POST', 'GET'])
def comments(request, review_pk):
    if request.method == 'GET':
        comments = Comment.objects.all().filter(review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        comment = Comment(user=request.user, content=request.data.get('content'), review=review)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)



@api_view(['PUT', 'DELETE'])
def comment_detail(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        if request.user == comment.user: # 글 작성자만 삭제 가능
            comment.delete()
            data = {
                'delete': f'{comment_pk}번 댓글이 성공적으로 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else: 
            data = {
                'delete': '권한이 없습니다.'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'PUT':
        if request.user == comment.user:
            comment.content = request.data.get('content')
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else: # 글 작성자가 아닐 때
            data = {
                'put': '권한이 없습니다.'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
