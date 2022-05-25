from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, MovieComment

User = get_user_model()

# 영화리스트
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'movie_num',)



# 영화상세정보
class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'first_name', 'gender', 'profile_image')
    movie_like = UserSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'



# 영화코멘트입력
class MovieCommentSerializer(serializers.ModelSerializer):

    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = '__all__'


    class Meta:
        model = MovieComment
        fields = '__all__'