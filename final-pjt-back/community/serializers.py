from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):           
        class Meta: 
            model = get_user_model()
            fields = ('username', 'first_name', 'gender', 'pk')
    
    user = UserSerializer()
    class Meta: 
        model = Comment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):           
        class Meta: 
            model = get_user_model()
            fields = ('username', 'first_name', 'gender', 'pk')
    
    comment_set = CommentSerializer(many=True)
    user = UserSerializer()

    class Meta: 
        model = Review
        fields = '__all__'
