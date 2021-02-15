from rest_framework import generics, status
from rest_framework.response import Response
from juntosegchallenge.settings import SECRET_KEY
from juntoseg.models import User
import jwt, datetime

class ConfirmAccountView(generics.GenericAPIView):
    
    def post(self, request):
        token = request.data.get('token', '')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'activation': 'Successfully activation'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as expired:
            print('Error >> ', expired)
            return Response({'activation': 'Expired Token'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as de:
            print('Error >> ', de)
            return Response({'activation': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)
