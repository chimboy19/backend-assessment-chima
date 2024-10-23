creat a folder  for the python app
Open cmd and navigate to the folder
the install virtualenv
name the virtual env appenv
navigate to the appenv scripts and  activate 
cd ../../ to back and folder address
now install django "pip install django"
after django-admin startproject  usermanagerapp
cd into the usermanagerapp 
typer python manage.py runserver 
control c and create a new app " python manage.py startapp users"
open the folder in your code-editor and  navigate to the app settings and  paste this "REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}"
Also add to the users app to your installed app in the settings
go back to the cmd and type"pip install djangorestframework_simplejwt"
navigate to user app  models.py and add this from django.contrib.auth.models import AbstractBaseUser , BaseUserManager   create your custom user  and super user and create the required models:
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.

class MyAccountManger(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('user must have an email address')
        
        if not username:
            raise ValueError('user must have  a username')
        
        user= self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,email,username,password):
        user=self.create_user(
              email=self.normalize_email(email),
              
               username=username,
               password=password,
               first_name=first_name,
               last_name=last_name,
        )

        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)

    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=MyAccountManger()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True





in cmd python manage.py makemigrations. then python manage.py migrate
then type python manage.py createsuperuser and fill in the required field
create a urls.py in the user app and add the following: from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
then add the following in the users app views.py :from rest_framework import generics, permissions
from .models import Account
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 5

class UserListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination

class UserDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

in the user app folder create serializers.py . in the serializers paste the following :from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Account
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 5

class UserListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination

class UserDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
