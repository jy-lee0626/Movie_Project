from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from movies.serializers import MovieSerializer
from movies.models import Movie
from community.models import Review
from .models import User

class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True)

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('movie_num', 'id', 'poster_path', )

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('id', 'title', 'created_at',)

    like_movies = MovieSerializer(many=True)
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'gender', 'like_movies', 'profile_image', 'review_set')

    def get_image_url(self, profile):
        request = self.context.get('request')
        photo_url = profile.profile_image.url
        return request.build_absolute_uri(photo_url)


class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image
    # profile_image = serializers.ImageField(use_url=True)
    gender = serializers.CharField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['gender'] = self.validated_data.get('gender')
        # data['profile_image'] = self.validated_data.get('profile_image', '')

        return data


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True)
    
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'gender', 'profile_image')