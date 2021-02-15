from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from juntoseg.models import User

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=255
    )
    token = serializers.CharField(
        max_length=68,
        min_length=8,
    )
    password = serializers.CharField(
        max_length=68,
        min_length=8,
        write_only=True
    )
    confirmPassword = serializers.CharField(
        max_length=68,
        min_length=8,
        write_only=True
    )


    def validate(self, attrs):
        password = attrs.get('password', '')
        confirmPassword = attrs.get('confirmPassword', '')
        email = attrs.get('email', '')
        token = attrs.get('token', '')

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print('Error >> ', e)
            raise serializers.ValidationError('This user does not exists')
        
        if password != confirmPassword:
            raise serializers.ValidationError('The passwords are different')

        valid = PasswordResetTokenGenerator().check_token(user, token)

        if not valid:
            raise serializers.ValidationError('Token is not valid, please request a new one')
        
        user.set_password(password)
        user.save()

        return (user)