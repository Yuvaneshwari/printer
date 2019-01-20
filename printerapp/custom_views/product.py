from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
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
def product_create(request):
    if request.method=='GET':
        return Response({'data':'','module':'Product'},template_name='product/product_create_update.html')
    else:
        pname=request.POST.get('product_name')
        gsizes=request.POST.getlist('sizes[]')
        gpapers=request.POST.getlist('papers[]')
        ggsms=request.POST.getlist('gsms[]')
        gprarray=request.POST.getlist('processidarray[]')
        sizes=list(map(int,gsizes))
        papers=list(map(int,gpapers))
        gsms=list(map(int,ggsms))
        prarray=list(map(int,gprarray))
        sizes_len=len(sizes)
        papers_len=len(papers)
        gsms_len=len(gsms)
        prarray_len=len(prarray)
        total_len=max(sizes_len,papers_len,gsms_len,prarray_len)
        data={"product_name":pname}
        productserializer=ProductSerializer(data=data)
        if productserializer.is_valid():
            productvar=productserializer.save();
            productid=productvar.id
            add_productdetails(sizes,papers,gsms,prarray,productid,total_len);
            if request.accepted_renderer.format=='html':
                return Response({"success_data": "Data added successfully"},template_name='product/product_create_update.html')
            return Response({"data": "Data added successfully"}, status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in productserializer.errors.keys():
                error_details.append({"field": key, "message": productserializer.errors[key][0]})
            data = {
            "Error": {
            "status": 400,
            "message": "Your submitted data was not valid - please correct the below errors",
            "error_details": error_details
            }
            }
            if request.accepted_renderer.format=='html':
                return Response({"error_data": data},template_name='product/product_create_update.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


def add_productdetails(sizes,papers,gsms,prarray,productid,total_len):
    for i in range(total_len):

        try:
            sizeval = sizes[i]
        except (IndexError, ValueError):
            sizeval = ''
        try:
            gsmval=gsms[i]
        except (IndexError, ValueError):
            gsmval = ''
        try:
            paperval = papers[i]
        except (IndexError, ValueError):
            paperval = ''
        try:
            prarrayval = prarray[i]
        except (IndexError, ValueError):
            prarrayval = '' 
        data={
            "product_size":sizeval,
            "productid":productid,
            "product_gsm":gsmval,
             "product_paper":paperval,
            "product_process":prarrayval,
        }
        proddetails_serializer=ProductdetailsSerializer(data=data)
        if proddetails_serializer.is_valid():
            proddetails_serializer.save()
        i+=1

@api_view(['GET','POST'])
def product_list(request):
    custom_filter={}
    custom_filter['deleted']=0
    product_obj = Product.objects.filter(**custom_filter)
    product_data = ProductSerializer(product_obj, many=True).data

    proddet_obj = Productdetails.objects.all()
    proddet_data = ProductdetailsSerializer(proddet_obj, many=True).data

    page = request.GET.get('page', 1)
    paginator = Paginator(product_data, row_per_page)
    try:
        product_data = paginator.page(page)
    except PageNotAnInteger:
        product_data = paginator.page(1)
    except EmptyPage:
        product_data = paginator.page(paginator.num_pages)
    
    if request.accepted_renderer.format == 'html':
        return Response({"data":product_data,"product_data":proddet_data},template_name='product/product_list.html')
    return Response({"data": product_data})

@api_view(['GET','POST'])
def product_view(request,id):
    product_obj = Product.objects.get(id=id)
    product_data = ProductSerializer(product_obj).data

    proddet_obj = Productdetails.objects.all()
    proddet_data = ProductdetailsSerializer(proddet_obj, many=True).data
    if request.accepted_renderer.format == 'html':
        return Response({"data":product_data,"product_data":proddet_data},template_name='product/product_create_update.html')
    return Response({"data": product_data})

@api_view(['GET', 'POST','Delete'])
def product_delete(request,id):
    selected_values=Product.objects.get(pk=id)
    selected_values.deleted=1;
    selected_values.save();
    return HttpResponseRedirect(reverse('printerapp:product_list'))

@api_view(['GET','PUT','POST'])
def product_update(request,id):
    product_obj=Product.objects.get(id=id)
    if request.method=='GET':
        data=ProductSerializer(product_obj).data

        proddet_obj = Productdetails.objects.all()
        proddet_data = ProductdetailsSerializer(proddet_obj, many=True).data

        if request.accepted_renderer.format == 'html':
            return Response({'data':data,"product_data":proddet_data},template_name='product/product_create_update.html')
        return Response({"data": data}, status=status.HTTP_200_OK)

    else:
        serializer=ProductSerializer(product_obj,request.data,partial=True)
        if serializer.is_valid():
            serializer.save();
            if request.accepted_renderer.format=='html':
                return HttpResponseRedirect(reverse('printerapp:product_list'))
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
                    return Response({"error_data": data},template_name='product/product_create_update.html')
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','POST'])
def product_processdelete(request,id):
    if request.method=='POST':
        print("hello")
        print(id)
        #print(productid)
        #selected_values=Productdetails.objects.get(pk=id)
        #selected_values.deleted=1;
        #selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:product_create_update'))

@api_view(['GET','PUT','POST'])
def product_processupdate(request):
    if request.method=='POST':
        print("hello")
        #print(id)
        #print(productid)
        #selected_values=Productdetails.objects.get(pk=id)
        #selected_values.deleted=1;
        #selected_values.save();
        return HttpResponseRedirect(reverse('printerapp:product_create'))
