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
from printerapp.custom_views.common_function import *



@api_view(['GET','POST'])
def employee_create(request):
    if request.method=='GET':
        user=session_user_id(request)
        login_username=user.username
        return Response({'data':'','module':'employee','login_username':login_username},template_name='employee/employee_create_update.html')
    else:
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='employee/employee_create_update.html')
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
                return Response({"error_data": data},template_name='employee/employee_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def employee_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    employee_obj = Employee.objects.filter(**custom_filter)
    employee_data = EmployeeSerializer(employee_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":employee_data,'module':'employee',"custom_filter":custom_filter},template_name='employee/employee_list.html')
    return Response({"data": employee_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def gsm_listdata(request):
    custom_filter={}
    custom_filter['deleted']=0
    gsm_obj = Gsm.objects.filter(**custom_filter)
    gsm_data = GsmSerializer(gsm_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":gsm_data,'module':'Gsm',"custom_filter":custom_filter},template_name='gsm/gsm_listdata.html')
    return Response({"data":gsm_data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def gsm_update(request,id):
    gsm_obj=Gsm.objects.get(id=id)
    if request.method=='GET':
        data=GsmSerializer(gsm_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='gsm/gsm_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

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
    selected_values=Gsm.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:gsm_list'))
