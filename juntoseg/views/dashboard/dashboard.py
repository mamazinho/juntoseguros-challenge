from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from juntoseg.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='dashboard.html'
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        profile = request.user
        return Response({'users': queryset, 'profile': profile})