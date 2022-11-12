from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import exceptions
from django.views.decorators.http import require_http_methods

class CustomLogin(ModelBackend):
    def userisExists(self, username):
        is_email = self.isEmail(username)
        user = get_user_model().objects.get(email=username) if is_email else get_user_model().objects.get(phone_no=username)
        if user:
            return True
        return False

    def isEmail(self, username):
        if '@' in username:
            return True
        return False 
    
    @require_http_methods(["POST"])
    def login():
        priit("login")

    def authenticate(self,request, username, password):
        print("custom authentication email={}".format(request.data['email']))
        email = request.data.get('email', None) # get email/phoneNo
        password = request.data.get('password', None)
        isEmailAddress = self.isEmail(email)
        if email is None or password is None:
            return None
        try:
           # login using phone and password
            userModel = get_user_model()
            if isEmailAddress:
                user = userModel.objects.get(email=email,password=password) 
                return user
            else:
                user = userModel.objects.get(phone_no=email,password=password)
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
