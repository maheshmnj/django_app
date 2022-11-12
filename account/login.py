from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions

class CustomLogin(authentication.BaseAuthentication):

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

    def authenticate(self, request):
        print("custom function email={}".format(request.data['email']))
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