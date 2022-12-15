from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User 

#Write the CustomBackend Model..

class UserBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        user_id = kwargs['username']
        password = kwargs['password']

        try:
            user = User.objects.get(username=user_id)
            if password == user.password:
                return user

        except User.DoesNotExist:
            return None
