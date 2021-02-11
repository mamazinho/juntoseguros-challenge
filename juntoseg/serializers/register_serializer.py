from rest_framework import serializers
from juntoseg.models import User

class RegisterSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        password = attrs.get('password', '')
        confirmPassword = attrs.get('confirmPassword', '')
        name = attrs.get('name', '')

        if not name.isalnum():
            raise serializers.ValidationError('Name should have only alphanumeric characters')
        if password != confirmPassword:
            raise serializers.ValidationError('The passwords are different')
        
        del attrs['confirmPassword']
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)