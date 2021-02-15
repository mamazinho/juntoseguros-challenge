from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from juntoseg.models import User

class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255
    )
    token = serializers.CharField(
        max_length=68,
        min_length=8,
        read_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'token']

    def validate(self, attrs):
        email = attrs.get('email', '')

        if not email:
            raise serializers.ValidationError('Email is required')

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print('Error >> ', e)
            raise serializers.ValidationError('This user does not exists')

        token = PasswordResetTokenGenerator().make_token(user)

        data = {
            'email': user.email,
            'token': token,
        }

        return data
