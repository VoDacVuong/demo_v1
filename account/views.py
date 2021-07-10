from typing import List
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from . import models
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import form
import json


def ListUser(req):
    users = list(models.myUser.objects.values())
    # print(dir(users))
    return JsonResponse({"data": users, 'messages': 'successfully', 'current_t': timezone.now()})


def UserDetail(req, key):
    flag = 0
    user = list(models.myUser.objects.values())
    for i in user:
        if(i['id'] == key):
            flag = 1
            return JsonResponse({"data": i, 'messages': 'successfully', 'current_t': timezone.now()})
    if(flag == 0):
        return JsonResponse({'messages': 'Not found ID', 'current_t': timezone.now()})


@csrf_exempt
def UpdateUser(req, key):
    if(req.method == "POST"):

        post_data = req.POST

        username = post_data.get("username")
        password = post_data.get("password")
        full_name = post_data.get("full_name")
        company_name = post_data.get("company_name")
        email = post_data.get("email")

        user = models.myUser.objects.get(id=key)
        user.username = username
        user.password = password
        user.full_name = full_name
        user.company_name = company_name
        user.email = email
        user.save()
        
        data = list(models.myUser.objects.values())
        for x in data:
            if x['id'] == key:
                return JsonResponse({"data": x, 'messages': 'successfully', 'current_t': timezone.now()})
    else:
        return JsonResponse({"data": "fail", 'messages': 'successfully', 'current_t': timezone.now()})


@csrf_exempt
def CreateUser(req):
    if(req.method == "POST"):
        data = req.POST

        user = models.myUser()
        user.username = data.get("username")
        user.password = data.get("password")
        user.company_name = data.get("company_name")
        
        # if data.is_valid():
        #     data.save()
        #     data = list(models.myUser.objects.values())
        #     return JsonResponse({"data": "", 'messages': 'successfully', 'current_t': timezone.now()})
        # else: JsonResponse({"data": "fail", 'messages': 'successfully', 'current_t': timezone.now()})




    
            
            







