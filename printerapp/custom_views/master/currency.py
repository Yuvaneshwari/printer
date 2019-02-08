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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

@api_view(['GET','POST'])
def currency_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Currency'},template_name='master/currency/currency_create_update.html')
    else:
        serializer=CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='master/currency/currency_create_update.html')
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
                return Response({"error_data": data},template_name='master/currency/currency_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def currency_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    currency_obj = Currency.objects.filter(**custom_filter)
    currency_data = CurrencySerializer(currency_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(currency_data, row_per_page)
    try:
        currency_data = paginator.page(page)
    except PageNotAnInteger:
        currency_data = paginator.page(1)
    except EmptyPage:
        currency_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":currency_data,'module':'Currency',"custom_filter":custom_filter},template_name='master/currency/currency_list.html')
    return Response({"data": currency_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def currency_view(request,id):
    currency_obj=Currency.objects.get(id=id)
    currency_data = CurrencySerializer(currency_obj).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":currency_data,'module':'Currency',"view_mode":1},template_name='master/currency/currency_create_update.html')
    return Response({"data":currency_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def currency_update(request,id):
    currency_obj=Currency.objects.get(id=id)
    if request.method=='GET':
        data=CurrencySerializer(currency_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='master/currency/currency_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=CurrencySerializer(currency_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:currency_list'))
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
                    return Response({"error_data": data},template_name='master/currency/currency_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def currency_delete(request,id):
    selected_values=Currency.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:currency_list'))
