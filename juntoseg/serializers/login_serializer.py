from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from juntoseg.models import User

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
    )
    password = serializers.CharField(
        max_length=68,
        min_length=8,
        write_only=True
    )
    tokens = serializers.CharField(
        max_length=68,
        min_length=8,
        read_only=True
    )

    class Meta:
        model = User
        fields = '__all__'

    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        print(attrs)
        user = authenticate(email=email, password=password)
        print(user)

        if not user:
            raise AuthenticationFailed('Invalid credentials (email or password)')
        elif not user.is_active:
            raise AuthenticationFailed('Active your account before login')

        data = {
            'email': user.email,
            'name': user.name,
            'tokens': user.tokens(),
        }

        return data