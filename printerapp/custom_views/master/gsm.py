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
def gsm_create(request):
    loginuser=session_user_id(request)
    print(loginuser)

    if request.method=='GET':
        if loginuser.has_perm('printerapp.add_gsm'):
            print("yes")
            return Response({'data':'','module':'Gsm'},template_name='gsm/gsm_create_update.html')
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')
    else:
        serializer=GsmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='gsm/gsm_create_update.html')
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
                return Response({"error_data": data},template_name='gsm/gsm_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def gsm_list(request):
    loginuser=session_user_id(request)
    print(loginuser)

    custom_filter={}
    custom_filter['deleted']=0
    gsm_obj = Gsm.objects.filter(**custom_filter)
    gsm_data = GsmSerializer(gsm_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(gsm_data, row_per_page)
    try:
        gsm_data = paginator.page(page)
    except PageNotAnInteger:
        gsm_data = paginator.page(1)
    except EmptyPage:
        gsm_data = paginator.page(paginator.num_pages)
    if loginuser.has_perm('printerapp.list_gsm'):
        print("yes")                
        if request.accepted_renderer.format == 'html':
            return Response({"data":gsm_data,'module':'Gsm',"custom_filter":custom_filter},template_name='gsm/gsm_list.html')
        return Response({"data": gsm_data}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')



@api_view(['GET'])
def gsm_view(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    gsm_obj=Gsm.objects.get(id=id)
    gsm_data = GsmSerializer(gsm_obj).data
    if loginuser.has_perm('printerapp.view_gsm'):
        print("yes")    
        if request.accepted_renderer.format == 'html':
            return Response({"data":gsm_data,'module':'Gsm',"view_mode":1},template_name='gsm/gsm_create_update.html')
        return Response({"data":gsm_data,"view_mode":1}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')



@api_view(['GET','PUT','POST'])
def gsm_update(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    gsm_obj=Gsm.objects.get(id=id)
    if request.method=='GET':
        data=GsmSerializer(gsm_obj).data
        if loginuser.has_perm('printerapp.change_gsm'):
            print("yes") 
            if request.accepted_renderer.format == 'html':
                return Response({'data':data},template_name='gsm/gsm_create_update.html')
            return Response({"data": data}, status=status.HTTP_200_OK)
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')


    else:
        serializer=GsmSerializer(gsm_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:gsm_list'))
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
                    return Response({"error_data": data},template_name='gsm/gsm_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def gsm_delete(request,id):
    loginuser=session_user_id(request)
    print(loginuser)
    if loginuser.has_perm('printerapp.delete_gsm'):
        print("yes")
        selected_values=Gsm.objects.get(pk=id)
        selected_values.deleted=1;
        selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:gsm_list'))
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')

