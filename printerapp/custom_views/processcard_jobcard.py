from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from printerapp.models import *
from printerapp.custom_views.common_function import *
from django.template.loader import render_to_string 
from printerapp.serializers.serializers import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from datetime import datetime

row_per_page=settings.GLOBAL_SETTINGS['row_per_page']


@api_view(['GET','POST'])
def processcard_create(request):
    processlist=[]
    jobcard="JOB023"
    jobcard_obj=Jobcard.objects.get(id=22)
    jobcard_data=JobcardSerializer(jobcard_obj).data

    for x in jobcard_data:
        print(x)
   
   
    jb_prd_obj=Jobcard_Product.objects.get(jobcardid=22)
    print("JOB023")

    jb_prd_obj2=Jobcard_Product_Process.objects.filter(jobcard_productid=jb_prd_obj.id)

    get_proccessids=Jobcard_Product_ProcessSerializer(jb_prd_obj2, many=True).data

    print(get_proccessids)
    for k in get_proccessids:
        for s,y in k.items():
            if(s=='processid'):
                get_process=Process.objects.get(id=y)
                processlist.append(get_process.process_name)

    get_prd_name=Product.objects.get(id=jb_prd_obj.productcard)
    prd_name=get_prd_name.product_name
    print(prd_name)
    print(processlist)

    mylist = zip(prd_name,processlist)
    if request.method=='GET':
        return Response({'data':'','jobcard':jobcard,'mylist':mylist,'customer':custname,'product':prd_name,'processlist':processlist},template_name='processcard/processcard1.html')

    if request.accepted_renderer.format == 'html':
        return Response({"data":process_data,'module':'Process',"custom_filter":custom_filter},template_name='productcard/product_list.html')
    return Response({"data": process_data}, status=status.HTTP_200_OK)

