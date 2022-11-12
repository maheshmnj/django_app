from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserPasswordResetSerializer, UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from account.models import User
import re

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]

  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'data': {'token': token}, 'success':True, 'client_msg':'Registration Successful', 'dev_msg':'Stored user in db active_ind'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  # function to check if the user exists
  def isEmail(self, username):
    isEmail = False
    if "@" in username:
       isEmail = True
    return isEmail

  def userExists(self, username):
    isEmail = self.isEmail(username)
    if isEmail:
      user = User.objects.filter(email=username)
    else:
      user = User.objects.filter(phone_no=username)
    if user:
      return True
    return False

  # function to login user
  def post(self, request, format=None):
    # serializer = UserLoginSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    # check if email or phone no exists
    # try:
    username = request.data['email']
    password = request.data['password']
    print("username={} password={}".format(username, password))
    if self.userExists(username):
      # if(self.isEmail(username)):
      #   colName = 'email'
      # else:
      #   colName = 'phone_no'
      # print("colName={}".format(colName))
      print("user exists")
      user = authenticate(request, email=username,password=password)
      if user:
        token = get_tokens_for_user(user)
        return Response({'data': {'token': token}, 'success':True, 'client_msg':'Login Successful', 'dev_msg':'User logged in'}, status=status.HTTP_200_OK)
      return Response({'data': {}, 'success':False, 'client_msg':'Invalid Credentials', 'dev_msg':'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)
    else:
      err_resp = {'success':False,'errors':{'email': ['User does not exist']}}
      return Response(err_resp, status=status.HTTP_404_NOT_FOUND)
    #     user = authenticate(email=username, password=password)
    #     if user:
    #       token = get_tokens_for_user(user)
    #       success_resp = {'data': {'token': token}, 'success':True, 'client_msg':'Login Successful', 'dev_msg':'Login Successful'}
    #       return Response(success_resp, status=status.HTTP_200_OK)
    #     else:
    #       print("invalid")
    #       error_resp = {'data': {}, 'success':False, 'client_msg':'Invalid Password', 'dev_msg':'Invalid Password'}
    #       return Response(error_resp, status=status.HTTP_400_BAD_REQUEST)
    # except:
   

def validateEmailAddress(email):
  # Regex to check valid email
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  # pass the regular expression
  # and the string in search() method
  if(re.search(regex,email)):
    return True
  else:
    return False

# class UserLoginView(APIView):
#   renderer_classes = [UserRenderer]
#   # function to check if the user exists
#   def post(self, request, format=None):
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')
#         # print("username:{} password: {}".format(username, password))
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             token = get_tokens_for_user(user)
#             return Response({'data':{'token':token}, 'success':True, 'client_msg':'Login Success', 'dev_msg':'Stored user in db active_ind'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    if serializer.is_valid(raise_exception=True):
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    if serializer.is_valid(raise_exception=True):
      return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

