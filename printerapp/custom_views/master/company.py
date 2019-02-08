from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from printerapp.models import *
from printerapp.serializers.serializers import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from printerapp.custom_views.common_function import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
row_per_page=settings.GLOBAL_SETTINGS['row_per_page']


@api_view(['GET','POST'])
def company_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Company'},template_name='master/company/company_create_update.html')
    else:
        print(request.data)
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            user_id= session_user_id(request)
            serializer.save(created_by=user_id,modified_date=store_date_time(),modified_by=user_id);
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='master/company/company_create_update.html')
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
                return Response({"error_data": data},template_name='master/company/company_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def company_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    company_obj = Company.objects.filter(**custom_filter)
    company_data = CompanySerializer(company_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(company_data, row_per_page)
    try:
        company_data = paginator.page(page)
    except PageNotAnInteger:
        company_data = paginator.page(1)
    except EmptyPage:
        company_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":company_data,'module':'Company',"custom_filter":custom_filter},template_name='master/company/company_list.html')
    return Response({"data":company_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def company_view(request,id):
    company_obj=Company.objects.get(id=id)
    company_data = CompanySerializer(company_obj).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":company_data,'module':'Company',"view_mode":1},template_name='master/company/company_create_update.html')
    return Response({"data":company_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def company_update(request,id):
    company_obj=Company.objects.get(id=id)
    if request.method=='GET':
        data=CompanySerializer(company_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='master/company/company_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=CompanySerializer(company_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:company_list'))
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
                    return Response({"error_data": data},template_name='master/company/company_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def company_delete(request,id):
    selected_values=Company.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:company_list'))
