from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from juntoseg.serializers import UserSerializer
from juntoseg.models import User

class DashboardView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = self.serializer_class(request.user)
        profile = serializer.data

        serializer = self.serializer_class(self.get_queryset(), many=True)
        users = serializer.data


        data = {
            'profile': profile, 
            'users': users
        }
        return Response(data, status.HTTP_200_OK)