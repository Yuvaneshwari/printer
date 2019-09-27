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
        get_custname=Customer.objects.get(id=jobcard_obj.customerid_id)
        customer=get_custname.name
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
        get_custname=Customer.objects.get(name=request.POST.get('custname'))
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
        print("ass")
        print(int(request.POST.get('assignto')))
        data={
        "jobcardid":int(request.POST.get('jobcardid')),
        "jobcard_productno":request.POST.get('productno'),
        "assigned_to":int(request.POST.get('assignto')),
        "customerid":customer,
        "productid":productname,
        "processid":process,
        "machine":int(request.POST.get('machine')),
        "supplierid":int(request.POST.get('supplier')),
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
    get_custname=Customer.objects.get(id=jobcard_obj.customerid_id)
    customer=get_custname.name
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



@api_view(['GET'])
def processcard_view(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    processcard_obj=Processcard.objects.get(id=id)
    data=ProcesscardSerializer(processcard_obj).data
        
    print("jobcardid")
    print(processcard_obj.jobcardid_id)
    print("productid")
    print(print(processcard_obj.productid_id))
    print("processid")
    print(processcard_obj.processid_id)
    print("customerid")
    print(processcard_obj.customerid_id)
    customer_obj=Customer.objects.get(id=processcard_obj.customerid_id)
    customer_data=CustomerSerializer(customer_obj).data
    print(customer_obj.name)
    comments_obj=Comments.objects.get(ref_id_id=id)
    comments_data=CommentsSerializer(comments_obj).data
    if loginuser.has_perm('printerapp.view_processcard'):
        print("yes")    
        if request.accepted_renderer.format == 'html':
            return Response({'data':data,'module':'Processcard','obj':processcard_obj,'comments_data':comments_data,'customer':customer_obj.name,"view_mode":1},template_name='processcard/processcard_update.html')
        return Response({"data":gsm_data,"view_mode":1}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')



@api_view(['GET','PUT','POST'])
def processcard_update(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    processcard_obj=Processcard.objects.get(id=id)
    data=ProcesscardSerializer(processcard_obj).data
        
    print("jobcardid")
    print(processcard_obj.jobcardid_id)
    print("productid")
    print(print(processcard_obj.productid_id))
    print("processid")
    print(processcard_obj.processid_id)
    print("customerid")
    print(processcard_obj.customerid_id)
    customer_obj=Customer.objects.get(id=processcard_obj.customerid_id)
    customer_data=CustomerSerializer(customer_obj).data
    print(customer_obj.name)
    comments_obj=Comments.objects.get(ref_id_id=id)
    comments_data=CommentsSerializer(comments_obj).data
    
    if request.method=='GET':
        if loginuser.has_perm('printerapp.change_processcard'):
            print("yes") 
            if request.accepted_renderer.format == 'html':
                return Response({'data':data,'module':'Processcard','obj':processcard_obj,'comments_data':comments_data,'customer':customer_obj.name},template_name='processcard/processcard_update.html')
            return Response({"data": data}, status=status.HTTP_200_OK)
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')


    else:
        print("enter")
        processcardid=int(id)

        data ={
            "comment":request.POST.get('comments'),
            "file":request.FILES.get('file_name'),
            "ref_id":processcardid,
            "ref_type":"1",
            }
        print(data)
        comments_obj = Comments.objects.get(ref_id_id=id)
        comments_data=CommentsSerializer(comments_obj,data=data,partial=True)
    
        if comments_data.is_valid():
            print("valid2")
            comments_data.save();
        #serializer=ProcesscardSerializer(processcard_obj,request.data,partial=True)
        #if serializer.is_valid():
            #serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:processcard_list'))
            return Response({"data": "Data Updated successfully"}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in serializer.errors.keys():
                error_details.append({"field": key, "message": serializer.errors[key][0]})
                data = {
                        "Error": {
                            "status": 400,
                            "message": "Your submitted data was not valid - please correct the below errors",
                            "error_details": error_details
                            }
                        }
                if request.accepted_renderer.format=='html':
                    return Response({"error_data": data},template_name='processcard/processcard_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def processcard_delete(request,id):
    loginuser=session_user_id(request)
    print(loginuser)
    if loginuser.has_perm('printerapp.delete_processcard'):
        print("yes")
        selected_values=Processcard.objects.get(pk=id)
        selected_values.deleted=1;
        selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:processcard_list'))
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')


@api_view(['GET'])
def processcard_list(request):
    loginuser=session_user_id(request)
    print(loginuser)

    custom_filter={}
    custom_filter['deleted']=0
    processcard_obj = Processcard.objects.filter(**custom_filter)
    processcard_data = ProcesscardSerializer(processcard_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(processcard_obj, row_per_page)
    try:
        processcard_data = paginator.page(page)
    except PageNotAnInteger:
        processcard_data = paginator.page(1)
    except EmptyPage:
        processcard_data = paginator.page(paginator.num_pages)
    if loginuser.has_perm('printerapp.list_processcard'):
        print("yes")                
        if request.accepted_renderer.format == 'html':
            return Response({"data":processcard_data,'module':'Processcard',"custom_filter":custom_filter},template_name='processcard/processcard_list.html')
        return Response({"data": processcard_data}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')

