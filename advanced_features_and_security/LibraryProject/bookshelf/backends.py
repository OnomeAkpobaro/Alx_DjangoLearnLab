from django.contrib.auth.backends import ModelBackend, BaseBackend
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import check_password


class ModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        return User
class CustomAuthenticationBackend(ModelBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    """
    def authenticate(self, request, username=None, password=None):
        login_valid = settings.ADMIN_LOGIN == username
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:

                user = User(username=username)
                user.is_staff =True
                user.is_superuser = True
                user.save()
            return None
        
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None