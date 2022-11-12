from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, phone_no,  password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          tc=tc,
          phone_no = phone_no,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, phone_no, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
          phone_no = phone_no,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,           # True: unique email ID for all users
  )
  name = models.CharField(max_length=200)
  phone_no = models.CharField(unique = True, max_length=10)
  tc = models.BooleanField()
  is_active = models.BooleanField(default=True)   # True: User will be active
  is_admin = models.BooleanField(default=False)   # False: After registration user should not become admin
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  id = models.IntegerField(primary_key=True, null=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'      # user can login using email only
  REQUIRED_FIELDS = ['name', 'tc', 'phone_no']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

#   def isUserExists(self, username):
      
  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin



