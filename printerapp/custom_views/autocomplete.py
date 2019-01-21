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
        users = Process.objects.filter(process_name__icontains = q )[:10]
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

            

