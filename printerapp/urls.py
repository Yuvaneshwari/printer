from django.conf.urls import url,include
from django.contrib import admin
from printerapp.views import *
from printerapp.custom_views import paper
from printerapp.custom_views import size
from printerapp.custom_views import gsm
from printerapp.custom_views import process
from printerapp.custom_views import product
from printerapp.custom_views import role
from printerapp.custom_views import employee
from printerapp.custom_views import autocomplete
from printerapp.custom_views.master import customergroup
from printerapp.custom_views.master import state
from printerapp.custom_views.master import currency
from printerapp.custom_views.master import company
from printerapp.custom_views.master import customer

app_name = 'printerapp'
urlpatterns = [	
    
 
    url(r'^home/$', create_home, name='home'),

    url(r'^login/$', login_user, name='login'),  
    url(r'^logout_user/$', logout_user, name='logout_user'),
    
    url(r'^user/user_list/$', user_list, name='user_list'),
    url(r'^user/user_update/(?P<id>[^/]*)/$', user_update, name='user_update'),
        
    url(r'^paper/paper_create/$', paper.paper_create, name='paper_create'),
    url(r'^paper/paper_list/$', paper.paper_list, name='paper_list'),
    url(r'^paper/paper_view/(?P<id>[^/]*)/$', paper.paper_view, name='paper_view'),
    url(r'^paper/paper_update/(?P<id>[^/]*)/$', paper.paper_update, name='paper_update'),
    url(r'^paper/paper_delete/(?P<id>[^/]*)/$', paper.paper_delete, name='paper_delete'),
    
    url(r'^size/size_create/$', size.size_create, name='size_create'),
    url(r'^size/size_list/$', size.size_list, name='size_list'),
    url(r'^size/size_view/(?P<id>[^/]*)/$', size.size_view, name='size_view'),
    url(r'^size/size_update/(?P<id>[^/]*)/$',size.size_update, name='size_update'),
    url(r'^size/size_delete/(?P<id>[^/]*)/$', size.size_delete, name='size_delete'),
	
	url(r'^gsm/gsm_create/$', gsm.gsm_create, name='gsm_create'),
    url(r'^gsm/gsm_list/$', gsm.gsm_list, name='gsm_list'),
    url(r'^gsm/gsm_view/(?P<id>[^/]*)/$', gsm.gsm_view, name='gsm_view'),
    url(r'^gsm/gsm_update/(?P<id>[^/]*)/$',gsm.gsm_update, name='gsm_update'),
    url(r'^gsm/gsm_delete/(?P<id>[^/]*)/$', gsm.gsm_delete, name='gsm_delete'),

    url(r'^process/process_create/$', process.process_create, name='process_create'),
    url(r'^process/process_list/$', process.process_list, name='process_list'),
    url(r'^process/process_view/(?P<id>[^/]*)/$', process.process_view, name='process_view'),
    url(r'^process/process_update/(?P<id>[^/]*)/$',process.process_update, name='process_update'),
    url(r'^process/process_delete/(?P<id>[^/]*)/$', process.process_delete, name='process_delete'),

    url(r'^product/product_create/$', product.product_create, name='product_create'),
    url(r'^autocomplete/processname/$', autocomplete.process_name_autocomplete, name='processname_auto'),
    url(r'^product/product_list/$', product.product_list, name='product_list'),
    url(r'^product/product_view/(?P<id>[^/]*)/$', product.product_view, name='product_view'),
    url(r'^product/product_delete/(?P<id>[^/]*)/$', product.product_delete, name='product_delete'),
    url(r'^product/product_update/(?P<id>[^/]*)/$', product.product_update, name='product_update'),
    url(r'^product/product_processdelete/(?P<id>[^/]*)/$', product.product_processdelete, name='product_processdelete'),
    url(r'^product/product_processupdate/$', product.product_processupdate, name='product_processupdate'),



    url(r'^customergroup/customergroup_create/$', customergroup.customergroup_create, name='customergroup_create'),
    url(r'^customergroup/customergroup_list/$', customergroup.customergroup_list, name='customergroup_list'),
    url(r'^customergroup/customergroup_view/(?P<id>[^/]*)/$', customergroup.customergroup_view, name='customergroup_view'),
    url(r'^customergroup/customergroup_update/(?P<id>[^/]*)/$',customergroup.customergroup_update, name='customergroup_update'),
    url(r'^customergroup/customergroup_delete/(?P<id>[^/]*)/$', customergroup.customergroup_delete, name='customergroup_delete'),

    url(r'^state/state_create/$', state.state_create, name='state_create'),
    url(r'^state/state_list/$', state.state_list, name='state_list'),
    url(r'^state/state_view/(?P<id>[^/]*)/$', state.state_view, name='state_view'),
    url(r'^state/state_update/(?P<id>[^/]*)/$',state.state_update, name='state_update'),
    url(r'^state/state_delete/(?P<id>[^/]*)/$', state.state_delete, name='state_delete'),

    url(r'^currency/currency_create/$', currency.currency_create, name='currency_create'),
    url(r'^currency/currency_list/$', currency.currency_list, name='currency_list'),
    url(r'^currency/currency_view/(?P<id>[^/]*)/$', currency.currency_view, name='currency_view'),
    url(r'^currency/currency_update/(?P<id>[^/]*)/$',currency.currency_update, name='currency_update'),
    url(r'^currency/currency_delete/(?P<id>[^/]*)/$', currency.currency_delete, name='currency_delete'),

    url(r'^company/company_create/$', company.company_create, name='company_create'),
    url(r'^company/company_list/$', company.company_list, name='company_list'),
    url(r'^company/company_view/(?P<id>[^/]*)/$', company.company_view, name='company_view'),
    url(r'^company/company_update/(?P<id>[^/]*)/$',company.company_update, name='company_update'),
    url(r'^company/company_delete/(?P<id>[^/]*)/$', company.company_delete, name='company_delete'),

    url(r'^customer/customer_create/$', customer.customer_create, name='customer_create'),
    url(r'^customer/customer_list/$', customer.customer_list, name='customer_list'),
    url(r'^customer/customer_view/(?P<id>[^/]*)/$', customer.customer_view, name='customer_view'),
    url(r'^customer/customer_update/(?P<id>[^/]*)/$',customer.customer_update, name='customer_update'),
    url(r'^customer/customer_delete/(?P<id>[^/]*)/$', customer.customer_delete, name='customer_delete'),

]