from django.shortcuts import get_object_or_404, render
from .models import Review, Comment
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
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'POST'])
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
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid() and request.user == review.user:
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == comment.user: # 글 작성자만 삭제 가능
            comment.delete()
            data = {
                'delete': f'{comment_pk}번 글이 성공적으로 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else: # 글 작성자가 아닐 때
            data = {
                'delete': '권한이 없습니다.'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'PUT':
        if request.user == comment.user: # 글 작성자만 수정 가능
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: # 글 작성자가 아닐 때
            data = {
                'put': '권한이 없습니다.'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_comment(request, article_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article_id=article_pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)