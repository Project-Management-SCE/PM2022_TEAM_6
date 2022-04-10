from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend, BaseBackend

from django.contrib.auth.models import User

from voulnteers.models import volnteer


class volnteerBackend(BaseBackend):

    # Create an authentication method
    # This is called by the standard Django login procedure

    def authenticate(self, request,username=None, psw=None,type=None):
        print("********************************")
        try:
            # Try to find a user matching your username
            user = volnteer.objects.get(username=username)

            #  Check the password is the reverse of the username
            if psw==user.password:
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except volnteer.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return volnteer.objects.get(pk=user_id)
        except volnteer.DoesNotExist:
            return None