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

@api_view(['GET','POST'])
def role_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Role'},template_name='role/role_create_update.html')
    else:
        print("enter")
        serializer=RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully",'module':'Role'},template_name='role/role_create_update.html')
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
                return Response({"error_data": data,'module':'Role'},template_name='role/role_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def role_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    role_obj = Role.objects.filter(**custom_filter)
    role_data = RoleSerializer(role_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":role_data,'module':'Role',"custom_filter":custom_filter},template_name='role/role_list.html')
    return Response({"data":role_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def role_listdata(request):
    custom_filter={}
    custom_filter['deleted']=0
    role_obj = Role.objects.filter(**custom_filter)
    role_data = RoleSerializer(role_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":role_data,'module':'Role',"custom_filter":custom_filter},template_name='role/role_listdata.html')
    return Response({"data":role_data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def role_update(request,id):
    role_obj=Role.objects.get(id=id)
    if request.method=='GET':
        data=RoleSerializer(role_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data,'module':'Role'},template_name='role/role_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=RoleSerializer(role_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:role_list'))
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
                    return Response({"error_data": data},template_name='role/role_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def role_view(request, id):
    data_obj = Role.objects.get(id=id)
    
    #loginuser=session_user_id(request)
    #print(loginuser)
    #print(loginuser.get_all_permissions())
    
    if request.method == "GET":
        #if loginuser.has_perm('ERP.view_permissions'):
            #print("yes")
        if request.accepted_renderer.format == 'html':
            return Response({"data": data_obj,"view_mode":1,'module':'Role'}, template_name='role/role_create_update.html')
        return Response({"data": ser_data,"view_mode":1}, status=status.HTTP_200_OK)
        #else:
            #print("no")
            #return Response({"data": ''}, template_name='includes/page_not_found.html')

@api_view(['GET', 'POST','Delete'])
def role_delete(request,id):
    selected_values=Role.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:role_list'))
