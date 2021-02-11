from rest_framework import serializers
from juntoseg.models import User

class ConfirmAccountSerializer(serializers.ModelSerializer):
    jwt_token = serializers.CharField(
        max_length=555,
    )

    class Meta:
        model = User
        fields = ['jwt_token']