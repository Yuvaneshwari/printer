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
        i=0
        process_list=[]
        productno_list=[]
        del_date_list=[]
        productname_list=[]
        jobcard=id
        jobcard_obj=Jobcard.objects.get(jobcard_no=jobcard)
        jobcardid=jobcard_obj.id
        print("jobcard")
        print(jobcard)
        get_custname=Customerdetails.objects.get(id=jobcard_obj.customerid_id)
        customer=get_custname.customer_name
        print("cust")
        print(customer)
        jb_prd_obj=Jobcard_Product.objects.filter(jobcardid=jobcardid)
        jb_prd_data = Jobcard_ProductSerializer(jb_prd_obj, many=True).data
        print("product")
        print(len(jb_prd_obj))
        productlen=len(jb_prd_obj)
        while(i<productlen):
            print(jb_prd_obj[i].product_no)
            print(jb_prd_obj[i].delivery_datetime)
            productno_list.append(jb_prd_obj[i].product_no)
            del_date_list.append(jb_prd_obj[i].delivery_datetime)
            get_prd=Product.objects.get(id=jb_prd_obj[i].productcard)
            productname_list.append(get_prd.product_name)

            i=i+1


        
    
        jb_prd_obj2=Jobcard_Product_Process.objects.filter(jobcard_productid=59)
        get_proccessids=Jobcard_Product_ProcessSerializer(jb_prd_obj2, many=True).data

        #print(get_proccessids)
        for k in get_proccessids:
            for s,y in k.items():
                if(s=='processid'):
                    get_process=Process.objects.get(id=y)
                    process_list.append(get_process.process_name)

        mylist=zip(productno_list,productname_list,del_date_list)       
        return Response({'data':'','jobcard':jobcard,'mylist':mylist,'productnolist':productno_list,'customer':customer,'product':productname_list,'processlist':process_list,'delivery_date':del_date_list},template_name='processcard/processcard1.html')
 