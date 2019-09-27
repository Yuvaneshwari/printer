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
from printerapp.custom_views.common_function import *

row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

@api_view(['GET','POST'])
def process_create(request):
    loginuser=session_user_id(request)
    print(loginuser)

    if request.method=='GET':
        if loginuser.has_perm('printerapp.add_process'):
            print("yes")
            return Response({'data':'','module':'Process'},template_name='process/process_create_update.html')
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')
    else:
        
        serializer=ProcessSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully",'module':'Process'},template_name='process/process_create_update.html')
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
                return Response({"error_data": data},template_name='process/process_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def process_list(request):
    loginuser=session_user_id(request)
    print(loginuser)

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
    if loginuser.has_perm('printerapp.list_process'):
        print("yes")
        if request.accepted_renderer.format == 'html':
            return Response({"data":process_data,'module':'Process',"custom_filter":custom_filter},template_name='process/process_list.html')
        return Response({"data": process_data}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')


@api_view(['GET'])
def process_view(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    process_obj=Process.objects.get(id=id)
    process_data = ProcessSerializer(process_obj).data
    if loginuser.has_perm('printerapp.view_process'):
        print("yes")
        if request.accepted_renderer.format == 'html':
            return Response({"data":process_data,'module':'Process',"view_mode":1,'obj':process_obj},template_name='process/process_create_update.html')
        return Response({"data":process_data,"view_mode":1}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')



@api_view(['GET','PUT','POST'])
def process_update(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    process_obj=Process.objects.get(id=id)
    if request.method=='GET':
        data=ProcessSerializer(process_obj).data
        if loginuser.has_perm('printerapp.change_process'):
            print("yes")
            if request.accepted_renderer.format == 'html':
                return Response({'data':data,'obj':process_obj},template_name='process/process_create_update.html')
            return Response({"data": data}, status=status.HTTP_200_OK)
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')
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
                    return Response({"error_data": data},template_name='process/process_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def process_delete(request,id):
    loginuser=session_user_id(request)
    print(loginuser)
    if loginuser.has_perm('printerapp.delete_process'):
        print("yes")
        selected_values=Process.objects.get(pk=id)
        selected_values.deleted=1;
        selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:process_list'))
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')


