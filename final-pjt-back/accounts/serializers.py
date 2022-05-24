from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'gender', 'like_movies', 'profile_image',)


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
        fields = '__all__'