import traceback

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from time import sleep

from juntoseg.models import User

import re
import json
from datetime import datetime, timedelta, date

class ResetPassword(View):
    

    def post(self, request):
        is_dev = ''
        referer = request.META.get('HTTP_REFERER')

        if re.compile(r'dev.rendasegura').search(referer):
            is_dev = 'dev'
        elif re.compile(r'beta.rendasegura').search(referer):
            is_dev = 'beta'

        email = json.loads(request.body).get('userEmail')
        result = {"code": 100}
        if not email:
            result["tip"] = "Preencha com o seu email"
            result["msg"] = "Ops, há um problema com seu e-mail"
            return JsonResponse(result, safe=False)

        else:
            user = User.objects.filter(email=email)
            
            if not user:            
                result["tip"] = "Não foi possível encontrar seu usuário"
                result["msg"] = "Ops, há um problema com seu usuário"
                return JsonResponse(result, safe=False)
            else:
                result["code"] = 200
                result["tip"] = "Instruções de recuperação foram enviadas para o seu email"
                result["msg"] = "Deu tudo certo"
                return JsonResponse(result, safe=False, status=result['code'])