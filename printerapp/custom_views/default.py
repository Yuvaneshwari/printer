from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from printerapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from printerapp.custom_views.common_function import *

@api_view(['GET','POST'])
def chk(request):
    if request.method=='GET':
        return Response({'data':''},template_name='includes/test_page.html')
    return Response({'data':'success'})




@api_view(['GET','POST'])
def create_home(request):
    loginuser=session_user_id(request)
    print(loginuser)
    user = User.objects.get(username=loginuser)
    print(user.id)

    size_create_perm = Permission.objects.get(name='Can add size')
    size_update_perm = Permission.objects.get(name='Can change size')
    size_delete_perm = Permission.objects.get(name='Can delete size')
    size_view_perm = Permission.objects.get(name='Can view size')
    size_list_perm = Permission.objects.get(name='Can list size')
    
    gsm_create_perm = Permission.objects.get(name='Can add gsm')
    gsm_update_perm = Permission.objects.get(name='Can change gsm')
    gsm_delete_perm = Permission.objects.get(name='Can delete gsm')
    gsm_view_perm = Permission.objects.get(name='Can view gsm')
    gsm_list_perm = Permission.objects.get(name='Can list gsm')
    

    paper_create_perm = Permission.objects.get(name='Can add paper')
    paper_update_perm = Permission.objects.get(name='Can change paper')
    paper_delete_perm = Permission.objects.get(name='Can delete paper')
    paper_view_perm = Permission.objects.get(name='Can view paper')
    paper_list_perm = Permission.objects.get(name='Can list paper')
    
    process_create_perm = Permission.objects.get(name='Can add process')
    process_update_perm = Permission.objects.get(name='Can change process')
    process_delete_perm = Permission.objects.get(name='Can delete process')
    process_view_perm = Permission.objects.get(name='Can view process')
    process_list_perm = Permission.objects.get(name='Can list process')
    
    product_create_perm = Permission.objects.get(name='Can add product')
    product_update_perm = Permission.objects.get(name='Can change product')
    product_delete_perm = Permission.objects.get(name='Can delete product')
    product_view_perm = Permission.objects.get(name='Can view product')
    product_list_perm = Permission.objects.get(name='Can list product')
    
    delivery_create_perm = Permission.objects.get(name='Can add deliverymode')
    delivery_update_perm = Permission.objects.get(name='Can change deliverymode')
    delivery_delete_perm = Permission.objects.get(name='Can delete deliverymode')
    delivery_view_perm = Permission.objects.get(name='Can view deliverymode')
    delivery_list_perm = Permission.objects.get(name='Can list deliverymode')
    

    communication_create_perm = Permission.objects.get(name='Can add communication')
    communication_update_perm = Permission.objects.get(name='Can change communication')
    communication_delete_perm = Permission.objects.get(name='Can delete communication')
    communication_view_perm = Permission.objects.get(name='Can view communication')
    communication_list_perm = Permission.objects.get(name='Can list communication')
    
    company_create_perm = Permission.objects.get(name='Can add company')
    company_update_perm = Permission.objects.get(name='Can change company')
    company_delete_perm = Permission.objects.get(name='Can delete company')
    company_view_perm = Permission.objects.get(name='Can view company')
    company_list_perm = Permission.objects.get(name='Can list company')
    
    jobcard_create_perm = Permission.objects.get(name='Can add jobcard')
    jobcard_update_perm = Permission.objects.get(name='Can change jobcard')
    jobcard_delete_perm = Permission.objects.get(name='Can delete jobcard')
    jobcard_view_perm = Permission.objects.get(name='Can view jobcard')
    jobcard_list_perm = Permission.objects.get(name='Can list jobcard')
    
    try:

        profile_user = Profile.objects.get(user_id=user.id)
        role = Role.objects.get(id=profile_user.role_id)
       
        if(role.size_create == 1):
            user.user_permissions.add(size_create_perm) 
        else:
            user.user_permissions.remove(size_create_perm) 
        if(role.size_update == 1):
            user.user_permissions.add(size_update_perm) 
        else:
            user.user_permissions.remove(size_update_perm) 
        if(role.size_delete == 1):
            user.user_permissions.add(size_delete_perm) 
        else:
            user.user_permissions.remove(size_delete_perm)                
        if(role.size_view == 1):
            user.user_permissions.add(size_view_perm) 
        else:
            user.user_permissions.remove(size_view_perm)                 
        if(role.size_list == 1):
            user.user_permissions.add(size_list_perm) 
        else:
            user.user_permissions.remove(size_list_perm) 
                

        if(role.gsm_create == 1):
            user.user_permissions.add(gsm_create_perm) 
        else:
            user.user_permissions.remove(gsm_create_perm) 
        if(role.gsm_update == 1):
            user.user_permissions.add(gsm_update_perm) 
        else:
            user.user_permissions.remove(gsm_update_perm) 
        if(role.gsm_delete == 1):
            user.user_permissions.add(gsm_delete_perm) 
        else:
            user.user_permissions.remove(gsm_delete_perm)                
        if(role.gsm_view == 1):
            user.user_permissions.add(gsm_view_perm) 
        else:
            user.user_permissions.remove(gsm_view_perm)                 
        if(role.gsm_list == 1):
            user.user_permissions.add(gsm_list_perm) 
        else:
            user.user_permissions.remove(gsm_list_perm) 
        

        if(role.paper_create == 1):
            user.user_permissions.add(paper_create_perm) 
        else:
            user.user_permissions.remove(paper_create_perm) 
        if(role.paper_update == 1):
            user.user_permissions.add(paper_update_perm) 
        else:
            user.user_permissions.remove(paper_update_perm) 
        if(role.paper_delete == 1):
            user.user_permissions.add(paper_delete_perm) 
        else:
            user.user_permissions.remove(paper_delete_perm)                
        if(role.paper_view == 1):
            user.user_permissions.add(paper_view_perm) 
        else:
            user.user_permissions.remove(paper_view_perm)                 
        if(role.paper_list == 1):
            user.user_permissions.add(paper_list_perm) 
        else:
            user.user_permissions.remove(paper_list_perm) 
        

        if(role.process_create == 1):
            user.user_permissions.add(process_create_perm) 
        else:
            user.user_permissions.remove(process_create_perm) 
        if(role.process_update == 1):
            user.user_permissions.add(process_update_perm) 
        else:
            user.user_permissions.remove(process_update_perm) 
        if(role.process_delete == 1):
            user.user_permissions.add(process_delete_perm) 
        else:
            user.user_permissions.remove(process_delete_perm)                
        if(role.process_view == 1):
            user.user_permissions.add(process_view_perm) 
        else:
            user.user_permissions.remove(process_view_perm)                 
        if(role.process_list == 1):
            user.user_permissions.add(process_list_perm) 
        else:
            user.user_permissions.remove(process_list_perm) 
        

        if(role.product_create == 1):
            user.user_permissions.add(product_create_perm) 
        else:
            user.user_permissions.remove(product_create_perm) 
        if(role.product_update == 1):
            user.user_permissions.add(product_update_perm) 
        else:
            user.user_permissions.remove(product_update_perm) 
        if(role.product_delete == 1):
            user.user_permissions.add(product_delete_perm) 
        else:
            user.user_permissions.remove(product_delete_perm)                
        if(role.product_view == 1):
            user.user_permissions.add(product_view_perm) 
        else:
            user.user_permissions.remove(product_view_perm)                 
        if(role.product_list == 1):
            user.user_permissions.add(product_list_perm) 
        else:
            user.user_permissions.remove(product_list_perm) 
        


        if(role.delivery_create == 1):
            user.user_permissions.add(delivery_create_perm) 
        else:
            user.user_permissions.remove(delivery_create_perm) 
        if(role.delivery_update == 1):
            user.user_permissions.add(delivery_update_perm) 
        else:
            user.user_permissions.remove(delivery_update_perm) 
        if(role.delivery_delete == 1):
            user.user_permissions.add(delivery_delete_perm) 
        else:
            user.user_permissions.remove(delivery_delete_perm)                
        if(role.delivery_view == 1):
            user.user_permissions.add(delivery_view_perm) 
        else:
            user.user_permissions.remove(delivery_view_perm)                 
        if(role.delivery_list == 1):
            user.user_permissions.add(delivery_list_perm) 
        else:
            user.user_permissions.remove(delivery_list_perm) 
        

        if(role.communication_create == 1):
            user.user_permissions.add(communication_create_perm) 
        else:
            user.user_permissions.remove(communication_create_perm) 
        if(role.communication_update == 1):
            user.user_permissions.add(communication_update_perm) 
        else:
            user.user_permissions.remove(communication_update_perm) 
        if(role.communication_delete == 1):
            user.user_permissions.add(communication_delete_perm) 
        else:
            user.user_permissions.remove(communication_delete_perm)                
        if(role.communication_view == 1):
            user.user_permissions.add(communication_view_perm) 
        else:
            user.user_permissions.remove(communication_view_perm)                 
        if(role.communication_list == 1):
            user.user_permissions.add(communication_list_perm) 
        else:
            user.user_permissions.remove(communication_list_perm) 
        

        if(role.company_create == 1):
            user.user_permissions.add(company_create_perm) 
        else:
            user.user_permissions.remove(company_create_perm) 
        if(role.company_update == 1):
            user.user_permissions.add(company_update_perm) 
        else:
            user.user_permissions.remove(company_update_perm) 
        if(role.company_delete == 1):
            user.user_permissions.add(company_delete_perm) 
        else:
            user.user_permissions.remove(company_delete_perm)                
        if(role.company_view == 1):
            user.user_permissions.add(company_view_perm) 
        else:
            user.user_permissions.remove(company_view_perm)                 
        if(role.company_list == 1):
            user.user_permissions.add(company_list_perm) 
        else:
            user.user_permissions.remove(company_list_perm) 
        

        if(role.jobcard_create == 1):
            user.user_permissions.add(jobcard_create_perm) 
        else:
            user.user_permissions.remove(jobcard_create_perm) 
        if(role.jobcard_update == 1):
            user.user_permissions.add(jobcard_update_perm) 
        else:
            user.user_permissions.remove(jobcard_update_perm) 
        if(role.jobcard_delete == 1):
            user.user_permissions.add(jobcard_delete_perm) 
        else:
            user.user_permissions.remove(jobcard_delete_perm)                
        if(role.jobcard_view == 1):
            user.user_permissions.add(jobcard_view_perm) 
        else:
            user.user_permissions.remove(jobcard_view_perm)                 
        if(role.jobcard_list == 1):
            user.user_permissions.add(jobcard_list_perm) 
        else:
            user.user_permissions.remove(jobcard_list_perm) 
        
    except Profile.DoesNotExist:
        print("no record")

    except Role.DoesNotExist:
        print("no record")
       
    if request.method=='GET':    
        return Response({'data':''},template_name='includes/home_page.html')
    return Response({'data':'success'})


@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'GET':
        return render(request, 'includes/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/printerapp/home/')
        return render(request, 'includes/login.html')

@api_view(['GET', 'POST'])
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('printerapp:login'))

@api_view(['GET'])
def user_list(request):
    custom_filter={}
    custom_filter['is_active']=1
    user_obj = User.objects.filter(**custom_filter)
    user_data = UserSerializer(user_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":user_data,'module':'User',"custom_filter":custom_filter},template_name='user/user_list.html')
    return Response({"data": user_data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT','POST'])
def user_update(request,id):
    user_obj=User.objects.get(id=id)
    
    profile_obj = Profile.objects.get(user=id)
    profile_data = ProfileSerializer(profile_obj).data
    
    if request.method=='GET':
        data=UserSerializer(user_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({'data':data,'module':'User','data_profile':profile_data},template_name='user/user_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        new_pwd=request.POST['password1']
        userobj=User.objects.get(id=id)
        userobj.set_password(new_pwd)    
        userobj.save()
       
        profile=Profile.objects.get(user=userobj.id)
        profile.role_id=request.POST['role']
        profile.save();
        return HttpResponseRedirect(reverse('printerapp:user_list'))



@api_view(['GET', 'POST'])
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            userobj=User.objects.get(username=username)
            userobj.save();
           
            role=request.POST['role']
            
            profile_data={                
                'role':role,
                'user':userobj.id
            }
            profile_serializer = ProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                print("profile serializer valid;")
                profile_serializer.save()

                
            return Response({"success_data": "Data Added Successfully", 'module':'User'},
                            template_name='user/user_create_update.html')
        else:
            error_details = []
            for key in form.errors.keys():
                error_details.append({"field": key, "message": form.errors[key][0]})
            
            data ={
            "Error": {
            "status": 400,
            "message": "Your submitted data was not valid - please correct the below errors",
            "error_details": error_details
            }
            }

            return Response({"error_data": data},
                            template_name='user/user_create_update.html')
    else:
        form = UserCreationForm()
    return render(request, 'user/user_create_update.html', {'form': form, 'module':'User'})
 


@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def user_delete(request,id):
    #loginuser=session_user_id(request)
    #print(loginuser)
    #print(loginuser.get_all_permissions())
    
    #if loginuser.has_perm('ERP.delete_user'):
        #print("yes")
    selected_values=User.objects.get(pk=id)
    selected_values.is_active=0
    selected_values.save();
    selected_profile=Profile.objects.get(user_id=id)
    selected_profile.deleted=1
    selected_profile.save();
    return HttpResponseRedirect(reverse('ERP:user_list'))    
    #else:
        #print("no")
        #return Response({"data": ''}, template_name='includes/page_not_found.html')



@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def user_view(request, id):
    data_obj = User.objects.get(id=id)
    
    #loginuser=session_user_id(request)
    #print(loginuser)
    #print(loginuser.get_all_permissions())
    
    profile_obj = Profile.objects.get(user=id)
    profile_data = ProfileSerializer(profile_obj).data
    
    if request.method == "GET":
        #if loginuser.has_perm('ERP.view_user'):
            #print("yes")
            if request.accepted_renderer.format == 'html':
                return Response({"data": data_obj,"view_mode":1,'module':'User','data_profile':profile_data}, template_name='user/user_create_update.html')
            return Response({"data": ser_data,"view_mode":1}, status=status.HTTP_200_OK)
        #else:
            #print("no")
            #return Response({"data": ''}, template_name='includes/page_not_found.html')
