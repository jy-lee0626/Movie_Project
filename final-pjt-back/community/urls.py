from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'), # 전체 리뷰 조회, 새 리뷰 생성
    path('reviews/<int:review_pk>', views.review_detail, name='review_detail'), # 리뷰 상세 조회, 수정, 삭제
    path('comments/<int:comment_pk>/', views.comment_detail),  # 댓글 조회, 수정, 삭제
    path('articles/<int:article_pk>/comments/', views.create_comment),  # 새 댓글 생성
]