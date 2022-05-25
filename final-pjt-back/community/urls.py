from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'), # 전체 리뷰 조회, 새 리뷰 생성
    path('reviews/<int:review_pk>', views.review_detail, name='review_detail'), # 리뷰 상세 조회, 수정, 삭제
    path('reviews/<int:review_pk>/like/', views.like_review, name='like_review'), # 리뷰 좋아요
    path('reviews/<int:review_pk>/comments/', views.comments),  # 전체 댓글 조회, 새 댓글 생성
    path('reviews/<int:review_pk>/comments/<int:comment_pk>', views.comment_detail),  # 댓글 수정, 삭제
]