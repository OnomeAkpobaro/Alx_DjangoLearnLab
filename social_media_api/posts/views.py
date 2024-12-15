from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for Post model handling CRUD operations
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title')
        content = self.request.query_params.get('content')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if content:
            queryset = queryset.filter(content__icontains=content)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for comment model handling CRUD operations
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class UserFeedView(APIView):
    """
    View to retrieve posts from followed users
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.users.is_following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LikePostView(APIView):
    """
    View to handle liking a post
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

            post = generics.get_object_or_404(Post, pk=pk)

            #check if user has already liked the post
            existing_like = Like.objects.filter(user=request.user, post=post)

            if existing_like.exists():
                return Response({"message": "Post already liked"}, status=status.HTTP_400_BAD_REQUEST)
            
            like = Like.objects.get_or_create(user=request.user, post=post)
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post
                )
                return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
                
           
        
class UnlikePostView(APIView):
    """
    View to handle unliking a post
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
     
            post = generics.get_object_or_404(Post, pk=pk)
            like = Like.objects.filter(user=request.user, post=post)
            if not like.exists():
                return Response({"error": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
            like.delete()
            return Response({"message": "Post Unliked"}, status=status.HTTP_204_NO_CONTENT)
           
                
        
    
