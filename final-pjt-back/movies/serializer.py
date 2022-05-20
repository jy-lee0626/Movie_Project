from rest_framework import serializers
from .models import Genre, Movie, MovieComment



# 영화리스트
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # 포스터만 보이게 할거면 title, genres 지워도 될 것 같음
        # 아니면 포스터에 마우스 올리면 제목, 장르 볼 수 있도록???
        fields = ('id', 'title', 'poster_path', 'genres',)



# 영화상세정보
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'



# 영화코멘트입력
class GetCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'



# 영화코멘트
class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'