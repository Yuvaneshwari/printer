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
import json

@api_view(['GET', 'POST'])
def process_name_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        custom_filter={}    
        custom_filter['deleted']=0 
        users = Process.objects.filter(process_name__icontains = q ,deleted=0)[:10]
        results = []
        for user in users:
            return_json = {}
            return_json['id'] = user.id
            return_json['label'] = user.process_name
            return_json['value'] = user.process_name
            
            
            results.append(return_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@api_view(['GET', 'POST'])
def product_name_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        custom_filter={}     
        custom_filter['deleted']=0
        users = Product.objects.filter(product_name__icontains = q,deleted=0 )[:10]
        results = []
        for user in users:
            return_json = {}
            return_json['id'] = user.id
            return_json['label'] = user.product_name
            return_json['value'] = user.product_name
            
            
            results.append(return_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
            

@api_view(['GET', 'POST'])
def customer_name_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        custom_filter={} 
        custom_filter['deleted']=0    
        users = Customer.objects.filter(name__icontains = q,deleted=0 )[:10]
        results = []
        #for user in users:
            #id=user.communication_mode_id
            #getid=Communication.objects.get(id=id)
            #print(getid.name)
        
        for user in users:
            return_json = {}
            return_json['id'] = user.id
            return_json['label'] = user.name
            return_json['value'] = user.name
            return_json['contact_person'] = user.contact_person
            return_json['primary_contact_no'] = user.primary_contact_no
            return_json['address'] = user.address
            return_json['email_id'] = user.email_id
            return_json['whatsup_no'] = user.whatsup_number
            return_json['secondary_contact_no'] = user.secondary_contact_no
            #return_json['communication_mode'] = getid.name
            
            #return_json['order_date'] = user.order_date

            results.append(return_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
            

@api_view(['GET', 'POST'])
def contact_no_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        custom_filter={}  
        custom_filter['deleted']=0   
        users = Customer.objects.filter(primary_contact_no__icontains = q )[:10]
        results = []
        for user in users:
            return_json = {}
            return_json['id'] = user.id
            return_json['label'] = user.primary_contact_no
            return_json['value'] = user.primary_contact_no
            return_json['customer_name'] = user.name
            return_json['contact_person'] = user.contact_person
            return_json['address'] = user.address
            return_json['email_id'] = user.email_id
            return_json['whatsup_no'] = user.whatsup_number
            return_json['secondary_contact_no'] = user.secondary_contact_no
            #return_json['communication_mode'] = user.communication_mode
            #return_json['order_date'] = user.order_date

           
            results.append(return_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
            
@api_view(['GET', 'POST'])
def user_name_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        custom_filter={}  
        custom_filter['deleted']=0   
        users = User.objects.filter(username__icontains = q,is_active=1)[:10]
        results = []
        for user in users:
            return_json = {}
            return_json['id'] = user.id
            return_json['label'] = user.username
            return_json['value'] = user.username
            
            
            results.append(return_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

