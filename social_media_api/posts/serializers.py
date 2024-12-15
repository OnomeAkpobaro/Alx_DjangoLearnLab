from rest_framework import serializers
from .models import Post, Comment, Like




class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']




class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_counts = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'content',
            'created_at', 'updated_at', 'comments',
            'likes_counts'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_likes_count(self,obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'created_at']
        