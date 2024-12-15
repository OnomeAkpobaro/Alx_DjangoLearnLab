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
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'password2', 'first_name', 'last_name']

    def validate(self, attrs):
        """
        Additional password validation
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password didn't match"})
        return attrs
    
    def create(self, validated_data):
        """
        Create a new user instance
        """

        validated_data.pop('password2')      #validate and remove 
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.save()
        Token.objects.create(user=user)
        return user
   
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
   


    def validate(self, attrs):
        """
        Validate user credentials
        """
        User = get_user_model()
        try:
            user = User.objects.get(email=attrs['email'])
            if not user.check_password(attrs['password']):
                raise serializers.ValidationError("Invalid Credentials")
            attrs['user'] = user
            return attrs
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

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
        return obj.get_followers_count() 
    def get_following_count(self, obj):
        return obj.get_following_count() 
    

    