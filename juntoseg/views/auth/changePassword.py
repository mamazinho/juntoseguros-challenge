import traceback
import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from datetime import datetime, timedelta, date
from juntoseg.models import User#, UserPasswordToken

#@method_decorator(csrf_exempt, name='dispatch')
class ChangePassword(View):

    def __check_token(self, token, user_id):
        user = User.objects.filter(id=user_id)
        if not user:
            return False
        else:
            usrPass = UserPasswordToken.objects.filter(user_id=user_id, token=token)
            if not usrPass:
                return False
            usrPass = usrPass[0]
            if usrPass.status != "Ativo":
                return False
            return usrPass

    # @check_jwt
    def post(self, request):
        data = json.loads(request.body)
        token, user_id = data.get("token", ""), data.get("userId", "")
        result = {"code": 100}
        
        userPassToken = self.__check_token(token, user_id)

        if not userPassToken:
            result["tip"] = "Esse token já expirou. Por favor, recupere a senha novamente."
            result["msg"] = "Erro no token"
            return JsonResponse(result, safe=False)

        else:
            email = userPassToken.user.email
            name = userPassToken.user.name
            passwd = data.get("userPwd", "")
            confirm_passwd = data.get("check_pwd", "")

            # password
            if not passwd:
                result["tip"] = "Preecha com uma senha(minimo 8 caracteres)"
                result["msg"] = "Temos um problema com sua senha!"
                return JsonResponse(result, safe=False)

            elif passwd != confirm_passwd:
                result["tip"] = "As senhas não coincidem"
                result["msg"] = "Temos um problema com sua senha!"
                return JsonResponse(result, safe=False)

            elif len(passwd) < 8:
                result["tip"] = "Senha muito curta, mínimo de 8 caracteres"
                result["msg"] = "Temos um problema com sua senha!"
                return JsonResponse(result, safe=False)

            else:
                userPassToken.user.set_password(passwd)
                userPassToken.user.save()
                userPassToken.status = 'Expirado'
                userPassToken.save()

                login(request, userPassToken.user)
                result["code"] = 200
                result["tip"] = f"Bem vindo de volta {name}!"
                result["msg"] = "Senha cadastrada com sucesso!"

                return JsonResponse(result, safe=False)
