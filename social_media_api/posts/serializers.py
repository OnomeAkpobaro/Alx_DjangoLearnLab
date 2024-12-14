from rest_framework import serializers
from .models import Post, Comment, Like




class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']