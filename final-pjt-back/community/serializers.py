from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Comment
        fields = '__all__'