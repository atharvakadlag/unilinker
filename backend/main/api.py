from rest_framework import viewsets, permissions
from main.serializers import UserSerializer, ProfileSerializer, LinkSerializer
from main.models import Profile, Link
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [permissions.AllowAny]
