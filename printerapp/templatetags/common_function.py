from django import template
register = template.Library()
from printerapp.models import *
from django.db import connection
from django.template import RequestContext        
from printerapp.serializers.serializers import *
from django.contrib.auth.models import User

@register.simple_tag
def sizelist(id):
	size_obj=Size.objects.get(id=id)
	return size_obj.size_name;

@register.simple_tag
def paperlist(id):
	paper_obj=Paper.objects.get(id=id)
	return paper_obj.paper_name;

@register.simple_tag
def gsmlist(id):
	gsm_obj=Gsm.objects.get(id=id)
	return gsm_obj.gsm_name;

@register.simple_tag
def processlist(id):
	process_obj=Process.objects.get(id=id)
	return process_obj.process_name;

@register.simple_tag
def userlist():
	user_obj=User.objects.all()
	user_data = UserSerializer(user_obj, many=True).data

	return user_data;

@register.simple_tag
def drop_down_list(tableName,show_field_name,store_field_name):
	data = []
	with connection.cursor() as cursor:
		query = "SELECT %s, %s FROM %s where deleted='0'" %(store_field_name,show_field_name,tableName)
		#return query
		cursor.execute(query)
		rows = cursor.fetchall()
		for obj in rows:
			data.append({"id":(obj[0]),"text":(obj[1])})
		return data


@register.simple_tag
def show_single_field(tableName,show_field_name,pk):
    data = []
    with connection.cursor() as cursor:
        if tableName and pk and show_field_name:
            query = "SELECT  `%s` FROM %s where id=%s" %(show_field_name,tableName,pk)
            #return query
            cursor.execute(query)
            row = cursor.fetchone()
            return row[0]


@register.simple_tag
def batch_drop_down_list(tableName,show_field_name,store_field_name,show_field_name1,show_field_name2):
	data = []
	with connection.cursor() as cursor:
		query = "SELECT %s, %s,%s,%s FROM %s where deleted='0'" %(store_field_name,show_field_name,show_field_name1,show_field_name2,tableName)
		#return query
		cursor.execute(query)
		rows = cursor.fetchall()
		for obj in rows:
			data.append({"id":(obj[0]),"text":(obj[1])+" -- "+(obj[2])+" -- "+(obj[3])})
		return data