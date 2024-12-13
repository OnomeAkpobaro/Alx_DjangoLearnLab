from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from  django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for User registrations with additional validations
    """
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = "__all__"

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
        user = get_user_model().objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password'],
            first_name=validate_data.get('first_name',''),
            last_name=validate_data.get('last_name', '')
        )

        Token.objects.create(user=user)
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
    

    