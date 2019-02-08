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
def pricingrule_paper(request):
    paperid= request.POST.get('paper')
    gsmid= request.POST.get('gsm')
    sizeid= request.POST.get('size')
    squareinch=int(request.POST.get('squareinch'))
    qty= int(request.POST.get('qty'))
    print(paperid)
    print(gsmid)
    print(sizeid)
    print(squareinch)
    print(qty)
    custom_filter={}
    custom_filter['deleted']=0
    custom_filter['papertype']=paperid
    custom_filter['gsm']=gsmid
    custom_filter['size']=sizeid
    
    paper_obj = Paperpricing.objects.filter(**custom_filter)
    paper_data = PaperpricingSerializer(paper_obj, many=True).data


    for x in paper_data:
        for s,y in x.items():
            if(s=='squareinch_from'):
                start=int(y)
            if(s=='squareinch_to'):
                end=int(y)
            if(s=='quality_from'):
                qty_start=int(y)
            if(s=='quality_to'):
                qty_end=int(y)
            if(s=='price'):
                getprice=int(y)
                #cal(squareinch,start,end,qty,qty_start,qty_end)
                if(squareinch>start and squareinch<end):
                    if(qty>qty_start and qty<qty_end):
                        print("yes")
                        result=getprice
                        break
                    else:
                        print("no")

                

    
    print(result)                    
    if request.accepted_renderer.format == 'html':
        return Response({"result":result},template_name='jobcard/jobcard1_create_update.html')
    return Response({"result": result})



def cal(squareinch,start,end,qty,qty_start,qty_end):
    if(squareinch>start and squareinch<end):
        if(qty>qty_start and qty<qty_end):
            print("yes")
    