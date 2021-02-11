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

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Email ou senha inválidas')
        elif not user.is_active:
            raise AuthenticationFailed('A conta está inativa, verifique o email enviado para ativação da conta')

        data = {
            'email': user.email,
            'name': user.name,
            'tokens': user.tokens(),
        }

        return data