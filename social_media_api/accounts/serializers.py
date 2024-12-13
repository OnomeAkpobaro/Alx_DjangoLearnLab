from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from  django.contrib.auth import get_user_model

User = get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for User registrations with additional validations
    """
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name', 'bio', 'profile_picture']

    def validate(self, attrs):
        """
        Additional password validation
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password didn't match"})
        return attrs
    
    def create(self, validate_data):
        """
        Create a new user instance
        """
        validate_data.pop('password2')      #validate and remove 
        user = User.objects.create_user(**validate_data)
        return user
    # def login(self, valid)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile details
    """
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers_count', 'following_count']
        read_only_fields = ['id']

    def get_followers_count(self, obj):
        return obj.get_followers_counts()
    def get_following_count(self, obj):
        return obj.get_following_count()
    

    