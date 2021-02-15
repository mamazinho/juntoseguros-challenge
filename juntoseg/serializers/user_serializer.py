from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from juntoseg.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']