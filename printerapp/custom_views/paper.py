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
def paper_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Paper'},template_name='paper/paper_create_update.html')
    else:
        serializer=PaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='paper/paper_create_update.html')
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
                return Response({"error_data": data},template_name='paper/paper_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def paper_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    paper_obj = Paper.objects.filter(**custom_filter)
    paper_data = PaperSerializer(paper_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(paper_data, row_per_page)
    try:
        paper_data = paginator.page(page)
    except PageNotAnInteger:
        paper_data = paginator.page(1)
    except EmptyPage:
        paper_data = paginator.page(paginator.num_pages)

    if request.accepted_renderer.format == 'html':
        return Response({"data":paper_data,'module':'Paper',"custom_filter":custom_filter},template_name='paper/paper_list.html')
    return Response({"data": paper_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def paper_view(request,id):
    paper_obj=Paper.objects.get(id=id)
    paper_data = PaperSerializer(paper_obj).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":paper_data,'module':'Paper',"view_mode":1},template_name='paper/paper_create_update.html')
    return Response({"data": paper_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def paper_update(request,id):
    paper_obj=Paper.objects.get(id=id)
    if request.method=='GET':
        data=PaperSerializer(paper_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data},template_name='paper/paper_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=PaperSerializer(paper_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:paper_list'))
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
                    return Response({"error_data": data},template_name='paper/paper_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def paper_delete(request,id):
    selected_values=Paper.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:paper_list'))
