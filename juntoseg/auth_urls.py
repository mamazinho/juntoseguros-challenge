from rest_framework.routers import DefaultRouter
from django.urls import path, include
from juntoseg.views import Challenge
from juntoseg.views.auth import *
from juntoseg.views.dashboard import *

router = DefaultRouter()

urlpatterns = [
    path('', Challenge.as_view(), name='challenge'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-account/', ConfirmAccountView.as_view(), name='confirm-account'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]


urlpatterns += router.urls