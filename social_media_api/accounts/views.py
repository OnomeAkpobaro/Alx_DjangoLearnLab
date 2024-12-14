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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
            print(token.key)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id':user.pk, 'username': user.username}, status=status.HTTP_200_OK)
            print (token.key)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProfileView(APIView):
    """
    View to retrieve and update user profile
    """
    permission_classes = [IsAuthenticated]

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

