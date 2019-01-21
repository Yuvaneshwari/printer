from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from printerapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from printerapp.custom_views.common_function import *


@api_view(['GET','POST'])
def create_home(request):
    if request.method=='GET':
        return Response({'data':''},template_name='includes/home_page.html')
    return Response({'data':'success'})


@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'GET':
        return render(request, 'includes/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/printerapp/home/')
        return render(request, 'includes/login.html')

@api_view(['GET', 'POST'])
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('printerapp:login'))

@api_view(['GET'])
def user_list(request):
    custom_filter={}
    user_obj = User.objects.filter(**custom_filter)
    user_data = UserSerializer(user_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":user_data,'module':'User',"custom_filter":custom_filter},template_name='user/user_list.html')
    return Response({"data": user_data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def user_update(request,id):
    user_obj=User.objects.get(id=id)
    if request.method=='GET':
        data=UserSerializer(user_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='user/user_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        userobj=User.objects.get(id=id)
        userobj.email=request.POST['email']
        userobj.first_name=request.POST['first_name']
        userobj.last_name=request.POST['last_name']
        userobj.is_active=1
        userobj.save()
        return HttpResponseRedirect(reverse('printerapp:user_list'))