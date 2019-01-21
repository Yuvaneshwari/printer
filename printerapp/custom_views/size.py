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
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

#from django.contrib.auth.backends import get_user_permissions

@api_view(['GET','POST'])
def size_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Size'},template_name='size/size_create_update.html')
    else:
        serializer=SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='size/size_create_update.html')
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
                return Response({"error_data": data},template_name='size/size_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def size_list(request):
    #get_perm = Permission.objects.get(name='Can add size')
    #get_user = User.objects.get(username='user4')
    #get_user.user_permissions.add(get_perm)
    #g_perm = Permission.objects.get(name='Can add log entry')
    #get_user.user_permissions.add(g_perm)
    #get_user.save()    
    custom_filter={}
    custom_filter['deleted']=0
    size_obj = Size.objects.filter(**custom_filter)
    size_data = SizeSerializer(size_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(size_data, row_per_page)
    try:
        size_data = paginator.page(page)
    except PageNotAnInteger:
        size_data = paginator.page(1)
    except EmptyPage:
        size_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":size_data,'module':'Size'},template_name='size/size_list.html')
    return Response({"data": size_data}, status=status.HTTP_200_OK)

    #userid=User.objects.get(username=loginuser)
    #print(userid.id)
    #chkperm=user_permissions.get(user=userid.id,permission=odd_even.id)
    #user = authenticate(user=userid.id,permission=odd_even.id)
    #print(chkperm)
    #if loginuser is not None:
        #print("confirm")
    #else:
        #print(user)
        #print("not")
    #uu= get_user_permissions(loginuser)
    
    #uu=loginuser.get_all_permissions()
    #print(uu)
    #uu1=loginuser.has_perm('printerapp.can_view_even_ids')
    #rint(uu1)
    

@permission_required('printerapp.add_size', login_url='/printerapp/size/size_list/')
def publish_blog(request):
    print("enter")
    return HttpResponse('checked')

@api_view(['GET'])
def size_view(request,id):
    size_obj=Size.objects.get(id=id)
    if request.method == "GET":
        size_data = SizeSerializer(size_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({"data":size_data,'module':'Size',"view_mode":1},template_name='size/size_create_update.html')
        return Response({"data":size_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def size_update(request,id):
    #loginuser=session_user_id(request)
    #print(loginuser)
    #print(loginuser.get_all_permissions())
    if request.method=='GET':
        #if loginuser.has_perm('printerapp.change_size'):
            #print("yes") 
            size_obj=Size.objects.get(id=id)
            data=SizeSerializer(size_obj).data
            if request.accepted_renderer.format == 'html':
                return Response({'data':data},template_name='size/size_create_update.html')
            return Response({"data": data}, status=status.HTTP_200_OK)
        #else:
            #print("no")
            #return Response({'data':''},template_name='includes/page_error.html')
    else:
        size_obj=Size.objects.get(id=id)
        serializer=SizeSerializer(size_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:size_list'))
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
                    return Response({"error_data": data},template_name='size/size_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
def size_delete(request,id):
    selected_values=Size.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:size_list'))
