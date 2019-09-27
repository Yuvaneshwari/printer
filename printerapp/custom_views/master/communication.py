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
from printerapp.custom_views.common_function import *

row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

@api_view(['GET','POST'])
def communication_create(request):
    loginuser=session_user_id(request)
    print(loginuser)

    if request.method=='GET':
        if loginuser.has_perm('printerapp.add_communication'):
            print("yes")    
            return Response({'data':'','module':'Communication'},template_name='master/communicationmode/communication_create_update.html')
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')
    else:
        serializer=CommunicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='master/communicationmode/communication_create_update.html')
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
                return Response({"error_data": data},template_name='master/communicationmode/communication_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def communication_list(request):
    loginuser=session_user_id(request)
    print(loginuser)

    custom_filter={}
    custom_filter['deleted']=0
    comm_obj = Communication.objects.filter(**custom_filter)
    comm_data = CommunicationSerializer(comm_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(comm_data, row_per_page)
    try:
        comm_data = paginator.page(page)
    except PageNotAnInteger:
        comm_data = paginator.page(1)
    except EmptyPage:
        comm_data = paginator.page(paginator.num_pages)
    if loginuser.has_perm('printerapp.list_communication'):
        print("yes")    
        if request.accepted_renderer.format == 'html':
            return Response({"data":comm_data,'module':'communication',"custom_filter":custom_filter},template_name='master/communicationmode/communication_list.html')
        return Response({"data":comm_data}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')

@api_view(['GET'])
def communication_view(request,id):
    loginuser=session_user_id(request)
    print(loginuser)

    comm_obj=Communication.objects.get(id=id)
    comm_data = CommunicationSerializer(comm_obj).data
    if loginuser.has_perm('printerapp.view_communication'):
        print("yes")
        if request.accepted_renderer.format == 'html':
            return Response({"data":comm_data,'module':'communication',"view_mode":1},template_name='master/communicationmode/communication_create_update.html')
        return Response({"data":comm_data,"view_mode":1}, status=status.HTTP_200_OK)
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')


@api_view(['GET','PUT','POST'])
def communication_update(request,id):
    loginuser=session_user_id(request)
    print(loginuser)
    comm_obj=Communication.objects.get(id=id)
    if request.method=='GET':
        data=CommunicationSerializer(comm_obj).data
        if loginuser.has_perm('printerapp.change_communication'):
            print("yes")    
            if request.accepted_renderer.format == 'html':
                return Response({'data':data},template_name='master/communicationmode/communication_create_update.html')
            return Response({"data": data}, status=status.HTTP_200_OK)
        else:
            print("no")
            return Response({'data':''},template_name='includes/page_not_found.html')
    else:
        serializer=CommunicationSerializer(comm_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:communication_list'))
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
                    return Response({"error_data": data},template_name='master/communicationmode/communication_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def communication_delete(request,id):
    loginuser=session_user_id(request)
    print(loginuser)
    if loginuser.has_perm('printerapp.delete_size'):
        print("yes")
        selected_values=Communication.objects.get(pk=id)
        selected_values.deleted=1;
        selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:communication_list'))
    else:
        print("no")
        return Response({'data':''},template_name='includes/page_not_found.html')

