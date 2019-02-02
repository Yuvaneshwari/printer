from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from printerapp.models import *
from django.template.loader import render_to_string 
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
def jobcard_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Productcard'},template_name='jobcard/jobcard1_create_update.html')
    else:
        print(request.data)
        serializer=ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='productcard/product_create_update.html')
            return Response({"data": "Data added successfully"}, status=status.HTTP_201_CREATED)
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


@api_view(['GET'])
def jobcard_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    process_obj = Process.objects.filter(**custom_filter)
    process_data = ProcessSerializer(process_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(process_data, row_per_page)
    try:
        process_data = paginator.page(page)
    except PageNotAnInteger:
        process_data = paginator.page(1)
    except EmptyPage:
        process_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":process_data,'module':'Process',"custom_filter":custom_filter},template_name='productcard/product_list.html')
    return Response({"data": process_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def jobcard_view(request,id):
    process_obj=Process.objects.get(id=id)
    process_data = ProcessSerializer(process_obj).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":process_data,'module':'Process',"view_mode":1},template_name='productcard/product_create_update.html')
    return Response({"data":process_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def jobcard_update(request,id):
    process_obj=Process.objects.get(id=id)
    if request.method=='GET':
        data=ProcessSerializer(process_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='productcard/product_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=ProcessSerializer(process_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:process_list'))
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
    selected_values=Process.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:process_list'))


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
        for k in get_process_data:
            for s,y in k.items():
                if(s=='product_process'):
                    get_process_id=Process.objects.get(id=y)
                    print(get_process_id.process_name)
                    processlist.append(get_process_id.process_name)
                    processid.append(get_process_id.id)
                    partialdelivery.append(get_process_id.is_deliveryTime)
          
        return Response({'processlist':processlist,'processid':processid,'partialdelivery':partialdelivery},template_name='jobcard/jobcard_create_update.html')


@api_view(['GET','PUT','POST'])
def getproductadd(request):
    html=None
    count=request.POST.get('count')
    print(count)
    if request.is_ajax():
        html = render_to_string("jobcard/jobcard1_add.html",{'data': count})
        return HttpResponse(html)
        

