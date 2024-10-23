from django.shortcuts import render

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