from rest_framework import serializers
from .models import UnilinkerUser


class UnilinkerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnilinkerUser
        fields = ['name', 'email', 'about_me', 'profile_pic', 'links']
