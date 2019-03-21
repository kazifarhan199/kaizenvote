from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class EmailBackend():
    def authenticate(self, request, username=None, password=None):
        try:
            email = username.lower()
            return User.objects.get(email=email)
        except Exception as e:
            print(e)
            return  None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None