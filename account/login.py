from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from rest_framework import exceptions
from django.views.decorators.http import require_http_methods

class CustomLogin(BaseBackend):
    def isEmail(self, username):
        if '@' in username:
            return True
        return False 

    def authenticate(self, request, username, password):
        print("custom authentication email={}".format(request.data['email']))
        isEmailAddress = self.isEmail(username)
        try:
           # login using phone and password
            userModel = self.get_user()
            print("isEmailAddress={}".format(isEmailAddress))
            if isEmailAddress:
                user = self.get_user().objects.get(email=email,password=password) 
                return user
            else:
                user = userModel.objects.get(phone_no=email,password=password)
                return user
        except:
            print("{} does not exist".format(username))
            return None

    def get_user(self, user_id):
        print("getting user")
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
