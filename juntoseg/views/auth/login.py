from rest_framework import generics, status
from rest_framework.response import Response
from juntoseg.models import User
from juntoseg.serializers import LoginSerializer
import datetime

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_200_OK)