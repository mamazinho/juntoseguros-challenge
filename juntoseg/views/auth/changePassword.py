from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from juntoseg.models import User
from juntoseg.serializers import ChangePasswordSerializer

class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': 'Password reset successfully'}, status.HTTP_200_OK)