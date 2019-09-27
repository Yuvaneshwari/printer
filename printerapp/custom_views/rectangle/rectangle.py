from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from printerapp.models import *
from printerapp.serializers.serializers import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

@api_view(['GET','POST'])
def logic_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Logic'},template_name='rectangle/logic.html')
    else:
        sheetlength=int(request.POST.get('sheetlength'))
        sheetwidth=int(request.POST.get('sheetwidth'))
        cardlength=int(request.POST.get('cardlength'))
        cardwidth=int(request.POST.get('cardwidth'))
        print(sheetlength)
        print(sheetwidth)
        print(cardlength)
        print(cardwidth)
        val=sheetlength%cardlength;
        if (val<cardwidth):
            rect=int((sheetlength/cardlength))*int((sheetwidth/cardwidth));
            print("IF BLOCK")
            print(rect)
        else:
            rect=(int(sheetlength/cardlength)*int(sheetwidth/cardwidth))+int(sheetwidth/cardlength);
            print("ELSE BLOCK")
            print(rect)

        if request.accepted_renderer.format=='html':
            return Response({"success_dat": "Data added successfully","rect":rect,"sheetlength":sheetlength,"sheetwidth":sheetwidth,"cardlength":cardlength,"cardwidth":cardwidth},template_name='rectangle/logic.html')
        return Response({"data": "Data added successfully","rect":rect}, status=status.HTTP_201_CREATED)
    
