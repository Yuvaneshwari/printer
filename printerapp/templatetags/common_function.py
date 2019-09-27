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
def productlist(id):
	product_obj=Product.objects.get(id=id)
	return product_obj.product_name;

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

@register.simple_tag
def getprocesslist(id):
	print(id)
	i=0
	process_list=[]
	default_user_id=[]
	default_user=[]
	machine1_list=[]
	machine2_list=[]
	machine3_list=[]
	machine4_list=[]
	machine5_list=[]

	user_obj=Jobcard_Product_Process.objects.filter(jobcard_productid=id)
	user_data = Jobcard_Product_ProcessSerializer(user_obj, many=True).data

	for k in user_data:
		for s,y in k.items():
			if(s=='processid'):
				get_process=Process.objects.get(id=y)
				process_list.append(get_process.process_name)
				machine1_list.append(get_process.machine1)
				machine2_list.append(get_process.machine2)
				machine3_list.append(get_process.machine3)
				machine4_list.append(get_process.machine4)
				machine5_list.append(get_process.machine5)
				
				if(get_process.default_user_id!=None):
					get_user=User.objects.get(id=get_process.default_user_id)
					default_user.append(get_user.username)
					default_user_id.append(get_process.default_user_id)
				else:
					default_user_id.append(i)
					default_user.append(i)

	print(process_list)
	print(default_user_id)
	print(default_user)
	get_process_list=zip(process_list,default_user,default_user_id,machine1_list,machine2_list,machine3_list,machine4_list,machine5_list)
	return get_process_list;


@register.simple_tag
def show_single_field_role(tableName,show_field_name,user):
    data = []
    with connection.cursor() as cursor:
        if tableName and user and show_field_name:
            query = "SELECT  `%s` FROM %s where user_id=%s" %(show_field_name,tableName,user)
            #return query
            cursor.execute(query)
            row = cursor.fetchone()
            return row[0]
