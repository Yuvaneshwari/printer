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
        productid_list=[]
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
        print(jb_prd_data)
        print(len(jb_prd_obj))
        productlen=len(jb_prd_obj)
        while(i<productlen):
            print(jb_prd_obj[i].product_no)
            print(jb_prd_obj[i].delivery_datetime)
            productid_list.append(jb_prd_obj[i].id)
            productno_list.append(jb_prd_obj[i].product_no)
            del_date_list.append(jb_prd_obj[i].delivery_datetime)
            get_prd=Product.objects.get(id=jb_prd_obj[i].productcard)
            productname_list.append(get_prd.product_name)

            i=i+1


        
    
        jb_prd_obj2=Jobcard_Product_Process.objects.filter(jobcard_productid=1)
        get_proccessids=Jobcard_Product_ProcessSerializer(jb_prd_obj2, many=True).data

        print(get_proccessids)
        for k in get_proccessids:
            for s,y in k.items():
                if(s=='processid'):
                    get_process=Process.objects.get(id=y)
                    process_list.append(get_process.process_name)

        print(process_list)
        mylist=zip(productno_list,productname_list,del_date_list,productid_list)   
        print("get")    
        return Response({'data':'','jobcard':jobcard,'jobcardid':jobcardid,'mylist':mylist,'productnolist':productno_list,'customer':customer,'product':productname_list,'processlist':process_list,'delivery_date':del_date_list},template_name='processcard/processcard1.html')
    else:
        
        print("enterrr")
        print(request.data)
        jobid=int(request.POST.get('jobcardid'))
        #print(request.POST.get('comments'))
        #print(request.POST.get('file'))
        #print(request.POST.get('custname'))
        #print(request.POST.get('prdname'))
        #print(request.POST.get('assignto'))
        #print(request.POST.get('date'))
        get_custname=Customerdetails.objects.get(customer_name=request.POST.get('custname'))
        customer=get_custname.id
        print("cust")
        print(customer)
        get_prd=Product.objects.get(product_name=request.POST.get('prdname'))
        productname=get_prd.id
        print(productname)
        get_process=Process.objects.get(process_name=request.POST.get('proname'))
        process=get_process.id
        jobcard_obj=Jobcard.objects.get(id=jobid)
        jobcard=jobcard_obj.jobcard_no
        data={
        "jobcardid":int(request.POST.get('jobcardid')),
        "jobcard_productno":request.POST.get('productno'),
        "assign_to":int(request.POST.get('assignto')),
        "customerid":customer,
        "productid":productname,
        "processid":process,
        "del_datetime":"2019-03-04 19:43:24"
        }
        print(data)
        proesscardserializer=ProcesscardSerializer(data=data)
        if proesscardserializer.is_valid():
            getprocesscardid=proesscardserializer.save();
            processcardid=getprocesscardid.id
            data ={
            "comment":request.POST.get('comments'),
            "file":request.FILES.get('file_name'),
            "ref_id":processcardid,
            "ref_type":"1",
            }
            commentsserializer = CommentsSerializer(data=data)
            if commentsserializer.is_valid():
                print("valid2")
                commentsserializer.save();
    print("post") 
    i=0
    process_list=[]
    productno_list=[]
    productid_list=[]
    del_date_list=[]
    productname_list=[]
    
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
    print(jb_prd_data)
    print(len(jb_prd_obj))
    productlen=len(jb_prd_obj)
    while(i<productlen):
        print(jb_prd_obj[i].product_no)
        print(jb_prd_obj[i].delivery_datetime)
        productid_list.append(jb_prd_obj[i].id)
        productno_list.append(jb_prd_obj[i].product_no)
        del_date_list.append(jb_prd_obj[i].delivery_datetime)
        get_prd=Product.objects.get(id=jb_prd_obj[i].productcard)
        productname_list.append(get_prd.product_name)

        i=i+1


        
    
    jb_prd_obj2=Jobcard_Product_Process.objects.filter(jobcard_productid=1)
    get_proccessids=Jobcard_Product_ProcessSerializer(jb_prd_obj2, many=True).data

    print(get_proccessids)
    for k in get_proccessids:
        for s,y in k.items():
            if(s=='processid'):
                get_process=Process.objects.get(id=y)
                process_list.append(get_process.process_name)

    print(process_list)
    mylist=zip(productno_list,productname_list,del_date_list,productid_list)   
    print("get")    
    return Response({'data':'','jobcard':jobcard,'jobcardid':jobcardid,'mylist':mylist,'productnolist':productno_list,'customer':customer,'product':productname_list,'processlist':process_list,'delivery_date':del_date_list},template_name='processcard/processcard1.html')
         

@api_view(['GET','POST'])
def comments_create(request,id):
    if request.method=='POST':
        print("enter")
        print(request.data)
       
        print(request.POST.get('comments'))
        print(request.POST.get('file'))
        print(request.POST.get('custname'))
        print(request.POST.get('prdname'))
        print(request.POST.get('assignto'))
        print(request.POST.get('date'))
        return Response({'data',''},template_name='processcard/processcard1.html')

