# from rest_framework import viewsets, permissions, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model
# from .serializers import UserProfileSerializer, UserRegistrationSerializer
# User = get_user_model()

# class UserViewset(viewsets.ModelViewSet):
#     """
    
#     """
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.AllowAny]
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions
from accounts.models import AccountUser



class RegisterView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id':user.pk, 'username': user.username}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProfileView(generics.GenericAPIViewe):
    """
    View to retrieve and update user profile
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserProfileSerializer(
            request.user, 
            data=request.data, 
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
        permission_classes = [permissions.IsAuthenticated]

        def post(self, request, user_id):
            try:
                user_to_follow = AccountUser.objects.get(id=user_id)
                if request.Accountuser.is_following(user_to_follow):
                    return Response({"detail": "Already following this user"}, status=status.HTTP_400_BAD_REQUEST)
                request.Accountuser.follow_user(user_to_follow)
                return Response({"detail": f" Now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
            except AccountUser.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfolow = AccountUser.objects.get(id=user_id)
            if not request.Accountuser.is_following(user_to_unfolow):
                return Response({"detail": "you are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
            request.Accountuser.unfollow(user_to_unfolow)
            return Response({"detail": f"you have unfollowed {user_to_unfolow.username}."}, status=status.HTTP_200_OK)
        except AccountUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
      
