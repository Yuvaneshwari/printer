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
def jobcard_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Jobcard'},template_name='jobcard/jobcard1_create_update.html')
    else:
        orderdate=request.POST.get("order_date")
        order_date=datetime.strptime(orderdate,"%m/%d/%Y").date()
        
        if not request.POST.get('customerid'):
            customer_name=request.POST.get("name")
            contact_person=request.POST.get("contact_person")
            primary_contact_no=request.POST.get("contact_no")
            whatsup_no=request.POST.get("whatsup_no")
            email_id=request.POST.get("email_id")
            secondary_contact_no=request.POST.get("sec_contact_no")
            address=request.POST.get("address")
            communication_mode=request.POST.get("communicationmode")
            
            data={
            "customer_name":customer_name,
            "contact_person":contact_person,
            "primary_contact_no":primary_contact_no,
            "whatsup_no":whatsup_no,
            "email_id":email_id,
            "secondary_contact_no":secondary_contact_no,
            "address":address,
            "communication_mode":communication_mode
            }
            customerserializer=CustomerdetailsSerializer(data=data)
            if customerserializer.is_valid():
                getcustomerid=customerserializer.save();
                getcustid=getcustomerid.id
        else:
            getcustid=request.POST.get('customerid')
        company_id=1
        series_type="JOB"
        series=create_jobcardno(company_id,series_type)
        data={"customerid":getcustid,"order_date":order_date,"jobcard_no":series}
        jobcardserializer=JobcardSerializer(data=data)
        if jobcardserializer.is_valid():
            getjobcardid=jobcardserializer.save();
            jobcardid=getjobcardid.id
            jobcardno=getjobcardid.jobcard_no
            print(jobcardid)
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully","jobcardid": jobcardid,"jobcardno":jobcardno},template_name='jobcard/jobcard1_create_update.html')
            return Response({"data": jobcardid,"jobcardid":jobcardid,"jobcardno":jobcardno}, status=status.HTTP_201_CREATED)
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
                return Response({"error_data": data},template_name='jobcard/jobcard1_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def jobcard_product_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Jobcard'},template_name='jobcard/jobcard1_create_update.html')
    else:
        jobcardid=request.POST.get("id")
        jobcardno=request.POST.get("jobcardno")
        pname=request.POST.get("Productname")
        paper=request.POST.get("Paper")
        gsm=request.POST.get("GSM")
        size=request.POST.get("Size")
        sizeselect=request.POST.get("Sizeselect")
        squareinch=request.POST.get("squareinch")
        quantity=request.POST.get("Quantity")
        partialdelivery=request.POST.get("PartialDelivery")
        partial_qty=request.POST.get("Partialqty")
        partial_datetime=request.POST.get("PartialDateTime")
        side=request.POST.get("Sides")
        jobtype=request.POST.get("Jobtype")
        delivery_mode=request.POST.get("Deliverymode")
        delivery_desc=request.POST.get("DeleiveryDesc")
        delivery_datetime=request.POST.get("DeleiveryDateTime")
        #productcardcount=request.POST.get("count")
        company_id=1
        series_type="PRD"
        productno=create_productno(company_id,series_type,jobcardno)
        print(productno)

        data={
        "productcard":pname,
        "size_custom":sizeselect,
        "squareinch":squareinch,
        "quantity":quantity,
        "partialdelivery":partialdelivery,
        "partial_qty":partial_qty,
        "partial_datetime":partial_datetime,
        "side":side,
        "delivery_mode":delivery_mode,
        "delivery_desc":delivery_desc,
        "delivery_datetime":delivery_datetime,
        "gsm":gsm,
        "jobcardid":jobcardid,
        "jobtype":jobtype,
        "paper":paper,
        "size":size,
        "product_no":productno
        }


        jobcard_productserializer=Jobcard_ProductSerializer(data=data)
        if jobcard_productserializer.is_valid():
            getjobcardproductid=jobcard_productserializer.save();
            jobcard_product_id=getjobcardproductid.id

            jobcard_product=getjobcardproductid.productcard
            product_obj=Product.objects.get(id=jobcard_product)
            print(product_obj.product_name)
            jobcard_product_name=product_obj.product_name
            #product_data = ProductSerializer(product_obj).data
            #jobcard_product_name=product_data.product_name

            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully",'jobcard_product_id':jobcard_product_id,"productno":productno,'productname':jobcard_product_name},template_name='jobcard/jobcard1_create_update.html')
            return Response({"data": '','jobcard_product_id':jobcard_product_id,'productno':productno,'productname':jobcard_product_name}, status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in jobcard_productserializer.errors.keys():
                error_details.append({"field": key, "message": serializer.errors[key][0]})
            data = {
            "Error": {
            "status": 400,
            "message": "Your submitted data was not valid - please correct the below errors",
            "error_details": error_details
            }
            }
            if request.accepted_renderer.format=='html':
                return Response({"error_data": data},template_name='jobcard/jobcard1_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def jobcard_product_process_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Jobcard'},template_name='jobcard/jobcard1_create_update.html')
    else:
        jobcard_product_id=request.POST.get("id")
        processlist_id=request.POST.getlist("processlist_id[]")
        process_ids=list(map(int,processlist_id))
        print(jobcard_product_id)
        print(process_ids)
        storeproduct_proccess(jobcard_product_id,process_ids)
        processname=[]
        for id in process_ids:
            process_obj=Process.objects.get(id=id)
            processname.append(process_obj.process_name)
        
        print(processname)
        if request.accepted_renderer.format=='html':
            return Response({"success_data": "Data added successfully",'jobcard_product_id':jobcard_product_id,'processlist':processname},template_name='processcard/processcard1.html')
        return Response({"data": '','jobcard_product_id':jobcard_product_id,'processlist':processname}, template_name='processcard/processcard1.html')
    
        #html=render_to_string("processcard/processcard1.html")
        #return HttpResponse(html)

    #return HttpResponse(reverse('printerapp:processcard_create'))
    return Response({"data": '','jobcard_product_id':jobcard_product_id,'processlist':processname}, template_name='processcard/processcard1.html')
        

    #return Response({"success_data": "Data added successfully"},template_name='processcard/processcard1.html')
    

def storeproduct_proccess(jobcard_product_id,process_ids):
    for x in process_ids:
        data ={
            "processid":x,
            "jobcard_productid":jobcard_product_id,
        }
        Product_process_serializer = Jobcard_Product_ProcessSerializer(data=data)
        if Product_process_serializer.is_valid():
            Product_process_serializer.save();



@api_view(['GET'])
def jobcard_list(request):
    custom_filter={}
    custom_filter['deleted']=0

    cust_obj = Customerdetails.objects.filter(**custom_filter)
    cust_data = CustomerdetailsSerializer(cust_obj, many=True).data


    jobcard_obj = Jobcard.objects.filter(**custom_filter)
    jobcard_data = JobcardSerializer(jobcard_obj, many=True).data

    product_obj = Jobcard_Product.objects.filter(**custom_filter)
    product_data = Jobcard_ProductSerializer(product_obj, many=True).data

    process_obj = Jobcard_Product_Process.objects.filter(**custom_filter)
    process_data = Jobcard_Product_ProcessSerializer(process_obj, many=True).data

    page = request.GET.get('page', 1)
    paginator = Paginator(jobcard_data, row_per_page)
    try:
        jobcard_data = paginator.page(page)
    except PageNotAnInteger:
        jobcard_data = paginator.page(1)
    except EmptyPage:
        jobcard_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":jobcard_data,'module':'Jobcard',"customerdata":cust_data,"jobcarddata":jobcard_data,"productdata":product_data,"processdata":process_data},template_name='jobcard/jobcard_list.html')
    return Response({"data":jobcard_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def jobcard_view(request,id):
    process_obj=Process.objects.get(id=id)
    process_data = ProcessSerializer(process_obj).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":process_data,'module':'Process',"view_mode":1},template_name='productcard/jobcard1_create_update.html')
    return Response({"data":process_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def jobcard_update(request,id):
    process_obj=Process.objects.get(id=id)
    if request.method=='GET':
        data=ProcessSerializer(process_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='productcard/jobcard1_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=ProcessSerializer(process_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:jobcard_list'))
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
                    return Response({"error_data": data},template_name='productcard/product_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def jobcard_delete(request,id):
    selected_values=Jobcard.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:jobcard_list'))

@api_view(['GET','PUT','POST'])
def getproductadd(request):
    html=None
    count=request.POST.get('count')
    print(count)
    if request.is_ajax():
        html = render_to_string("jobcard/jobcard1_add.html",{'data': count})
        return HttpResponse(html)
 
@api_view(['GET','POST'])
def getprocesslist(request):

    if request.method=='POST':
        get_productid=request.POST.get('productid')
        custom_filter={}
        custom_filter['productid']=get_productid
        get_process_obj=Productdetails.objects.filter(**custom_filter)
        get_process_data = ProductdetailsSerializer(get_process_obj, many=True).data
        processlist=[]
        processid=[]
        partialdelivery=[]
        defaultprocess=[]
        for k in get_process_data:
            for s,y in k.items():
                if(s=='product_process'):
                    get_process_id=Process.objects.get(id=y)
                    processlist.append(get_process_id.process_name)
                    processid.append(get_process_id.id)
                    partialdelivery.append(get_process_id.is_deliveryTime)
                if(s=='default_process'):
                    defaultprocess.append(y)

        
        return Response({'processlist':processlist,'processid':processid,'partialdelivery':partialdelivery,'defaultprocess':defaultprocess},template_name='jobcard/jobcard_create_update.html')


       

@api_view(['GET','POST'])
def getsizevalues(request):

    if request.method=='POST':
        get_sizeid=request.POST.get('sizeid')
        get_size_obj=Size.objects.get(id=get_sizeid)
    
        
        return Response({'length':get_size_obj.length,'width':get_size_obj.width},template_name='jobcard/jobcard_create_update.html')


@api_view(['GET','POST'])
def resetseries(request):
    custom_filter={}
    series_for="PRD"
    custom_filter['series_for']=series_for
    series_det=Series.objects.get(series_for=series_for)
    if series_det:
        series_det.series_count=0
        series_det.save()
   
    return Response({"data": ''}, status=status.HTTP_201_CREATED)    