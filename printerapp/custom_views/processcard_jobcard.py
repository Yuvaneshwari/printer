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
def processcard_create(request,id):
    if request.method=='GET':
        
        processlist=[]
        jobcard=id
        jobcard_obj=Jobcard.objects.get(jobcard_no=jobcard)
        jobcardid=jobcard_obj.id
       
        get_custname=Customerdetails.objects.get(id=jobcard_obj.customerid_id)
        customer=get_custname.customer_name

        jb_prd_obj=Jobcard_Product.objects.get(jobcardid=jobcardid)
        del_date=jb_prd_obj.delivery_datetime

        get_prd=Product.objects.get(id=jb_prd_obj.productcard)
        prd_name=get_prd.product_name

        jb_prd_obj2=Jobcard_Product_Process.objects.filter(jobcard_productid=jb_prd_obj.id)
        get_proccessids=Jobcard_Product_ProcessSerializer(jb_prd_obj2, many=True).data

        #print(get_proccessids)
        for k in get_proccessids:
            for s,y in k.items():
                if(s=='processid'):
                    get_process=Process.objects.get(id=y)
                    processlist.append(get_process.process_name)

       
        return Response({'data':'','jobcard':jobcard,'customer':customer,'product':prd_name,'processlist':processlist,'delivery_date':del_date},template_name='processcard/processcard1.html')
 