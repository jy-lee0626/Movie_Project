from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model


class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):           
        class Meta: 
            model = get_user_model()
            fields = ('username', 'first_name', 'gender', 'pk','profile_image')
    
    user = UserSerializer()
    class Meta: 
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ProfileSerializer(serializers.ModelSerializer):
        profile_image = serializers.ImageField(use_url=True)
        class Meta:
            model = get_user_model()
            fields = ('username', 'first_name', 'gender', 'pk', 'profile_image')
    
    user = ProfileSerializer()
    class Meta: 
        model = Comment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):           
        class Meta: 
            model = get_user_model()
            fields = ('username', 'first_name', 'gender', 'pk','profile_image')
    
    comment_set = CommentSerializer(many=True)
    user = UserSerializer()
    like_users = UserSerializer(many=True)

    class Meta: 
        model = Review
        fields = '__all__'
