from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from printerapp.models import *


class Paper(models.Model):
    """Details of Paper Entity"""
    paper_name = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Paper_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Paper_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("paper_name"),
        ]


class Size(models.Model):
    """Details of Size Entity"""
    size_name = models.CharField(max_length=50, blank=False, null=False)
    length = models.CharField(max_length=50,blank=True, null=True)
    width = models.CharField(max_length=50,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Size_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Size_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("size_name"),
        ]
        permissions = (
            ('can_view_odd_ids', 'can_view_odd_ids'),
            ('can_view_even_ids', 'can_view_even_ids'),)

class Gsm(models.Model):
    """Details of Gsm Entity"""
    gsm_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Gsm_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Gsm_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("gsm_name"),
        ]

class Process(models.Model):
    """Details of process Entity"""
    process_name = models.CharField(max_length=50, blank=False, null=False)
    is_deliveryTime=models.BooleanField(default=False)
    machine1=models.BooleanField(default=False)
    machine2=models.BooleanField(default=False)
    machine3=models.BooleanField(default=False)
    machine4=models.BooleanField(default=False)
    machine5=models.BooleanField(default=False)
    default_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='Process_default_User',blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Process_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Process_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("process_name"),
        ]

class Product(models.Model):
    """Details of process Entity"""
    product_name = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Product_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Product_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("product_name"),
        ]

class Productdetails(models.Model):
    productid=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pd_productid')
    product_process=models.ForeignKey(Process, on_delete=models.CASCADE, related_name='pd_process',null=True,blank=True)
    default_process=models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)




class CustomerGroup(models.Model):
    """docstring for CustomerGroup"""
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='CustomerGroup_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='CustomerGroup_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("name", "deleted"),
        ]

class StateMaster(models.Model):
    """docstring for StateMaster"""
    state = models.CharField(max_length=50, null=False, blank=False)
    state_code = models.CharField(max_length=50, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='StateMaster_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='StateMaster_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("state", "state_code","deleted"),
        ]

class Currency(models.Model):
    """Details of Currency Entity"""
    name = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Currency_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Currency_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("name", "country","deleted"),
        ]

class Company(models.Model):
    """Details of Company Entity"""
    name = models.CharField(max_length=50, blank=True, null=False)
    short_name = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=300, blank=True, null=False)
    gst_no = models.CharField(max_length=30 ,null=True)
    cst_no = models.CharField(max_length=30, null=True)
    tin_no = models.CharField(max_length=30 ,null=True)
    pan_no = models.CharField(max_length=10 ,null=True)
    bank_name = models.TextField(max_length=50, blank=True, null=False)
    account_holder_name = models.TextField(
        max_length=50, blank=False, null=False)
    account_no = models.CharField(blank=True, null=True,max_length=25)
    ifsc_code = models.TextField(max_length=30, blank=True, null=True)
    default_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='Company_Currency',default=None)
    state= models.ForeignKey(
        StateMaster, on_delete=models.CASCADE, related_name='Company_State',default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Company_Created_By_User', default=None)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Company_Modified_By_User', default=None)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("name", "short_name","deleted"),
        ]


class Communication(models.Model):
    """Details of Communication Entity"""
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Communication_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Communication_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("name"),
        ]

class Customer(models.Model):
    """docstring for Customer"""
    name = models.CharField(max_length=100,blank=True, null=True)
    customergroup = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE,default=1)
    primary_contact_no = models.CharField(max_length=50,blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    contact_person = models.CharField(max_length=50,blank=True, null=True)
    contact_person_contact_no = models.CharField(max_length=50,blank=True, null=True)
    contact_person_email_id = models.EmailField(max_length=50,blank=True, null=True)
    secondary_contact_no = models.CharField(max_length=50,blank=True, null=True)
    secondary_email_id = models.EmailField(blank=True, null=True)
    referred_by = models.IntegerField(default=False)
    address = models.CharField(max_length=200,blank=True, null=True)
    state= models.ForeignKey(StateMaster, on_delete=models.CASCADE, related_name='customer_State',default=1)
    max_credit_amount = models.IntegerField(default=0)
    credit_days = models.IntegerField(default=0)
    credit_status = models.CharField(max_length=30,blank=True, null=True)
    billing_address = models.CharField(max_length=200,blank=True, null=True)
    shiping_address = models.CharField(max_length=200,blank=True, null=True)
    gst_no = models.CharField(max_length=20,blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default=1)
    default_cash_customer=models.IntegerField(default=0)
    whatsup_number=models.CharField(max_length=30,blank=True, null=True)
    communication_mode=models.ForeignKey(Communication, on_delete=models.CASCADE, related_name='communication_mode_customer',default=1)    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customer_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    unique_together = [
            ("name", "primary_contact_no","deleted","company"),
        ]

class Deliverymode(models.Model):
    """Details of Deliverymode Entity"""
    deliverymode = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Deliverymode_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Deliverymode_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("deliverymode"),
        ]


class Jobtype(models.Model):
    """Details of Paper Entity"""
    jobtype_name = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Jobtype_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Jobtype_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("jobtype_name"),
        ]

class Paperpricing(models.Model):
    """Details of Paperpricing Entity"""
    papertype = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='papertype', default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size', default=1)
    gsm =models.ForeignKey(Gsm, on_delete=models.CASCADE, related_name='gsm', default=1)
    squareinch_from=models.CharField(max_length=50)
    squareinch_to=models.CharField(max_length=50)
    quality_from=models.CharField(max_length=50)
    quality_to=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Paperpricing_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Paperpricing_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Packingpricing(models.Model):
    """Details of Packingpricing Entity"""
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='packing_size', default=1)
    quantity_from=models.IntegerField(default=0)
    quantity_to=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Packingpricing_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Packingpricing_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Processpricing(models.Model):
    """Details of Processpricing Entity"""
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='process', default=1)
    jobtype = models.IntegerField(default=0)
    pricingtype =models.IntegerField(default=0)
    time_squareinch_from=models.IntegerField(default=0)
    time_squareinch_to=models.IntegerField(default=0)
    time_hour_from=models.IntegerField(default=0)
    time_hour_to=models.IntegerField(default=0)
    time_price=models.IntegerField(default=0)
    
    qty_squareinch_from=models.IntegerField(default=0)
    qty_squareinch_to=models.IntegerField(default=0)
    qty_from=models.IntegerField(default=0)
    qty_to=models.IntegerField(default=0)
    qty_price=models.IntegerField(default=0)
    
    pages_squareinch_from=models.IntegerField(default=0)
    pages_squareinch_to=models.IntegerField(default=0)
    pages_from=models.IntegerField(default=0)
    pages_to=models.IntegerField(default=0)
    pages_price=models.IntegerField(default=0)
    
    size_squareinch_from=models.IntegerField(default=0)
    size_squareinch_to=models.IntegerField(default=0)
    size_price=models.IntegerField(default=0)
    
    cycle_squareinch_from=models.IntegerField(default=0)
    cycle_squareinch_to=models.IntegerField(default=0)
    cycle_from=models.IntegerField(default=0)
    cycle_to=models.IntegerField(default=0)
    cycle_price=models.IntegerField(default=0)
   
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Processpricing_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Processpricing_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Bytime(models.Model):
    Processpricing = models.ForeignKey(Processpricing, on_delete=models.CASCADE, related_name='processpricing_bt', default=1)
    squareinch_from=models.CharField(max_length=50,blank=True, null=True)
    squareinch_to=models.CharField(max_length=50,blank=True, null=True)
    time_from=models.CharField(max_length=50,blank=True, null=True)
    time_to=models.CharField(max_length=50,blank=True, null=True)
    time_price=models.CharField(max_length=50,blank=True, null=True)
    deleted = models.BooleanField(default=False)

class Byquantity(models.Model):    
    Processpricing = models.ForeignKey(Processpricing, on_delete=models.CASCADE, related_name='processpricing_bq', default=1)
    size_qty = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size_quantity', default=1)
    quality_from=models.CharField(max_length=50,blank=True, null=True)
    quality_to=models.CharField(max_length=50,blank=True, null=True)
    price_qty=models.CharField(max_length=50,blank=True, null=True)
    deleted = models.BooleanField(default=False)

class Bynopages(models.Model):
    Processpricing = models.ForeignKey(Processpricing, on_delete=models.CASCADE, related_name='processpricing_bp', default=1)
    size_qty = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size_nopages', default=1)
    nopages=models.CharField(max_length=50,blank=True, null=True)
    price_nopages=models.CharField(max_length=50,blank=True, null=True)
    deleted = models.BooleanField(default=False)

class Customerdetails(models.Model):
    """docstring for Customerdetails"""
    customer_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50,blank=True, null=True)
    primary_contact_no = models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    whatsup_no = models.CharField(max_length=50,blank=True, null=True)
    secondary_contact_no = models.CharField(max_length=50,blank=True, null=True)
    communication_mode=models.ForeignKey(Communication, on_delete=models.CASCADE, related_name='communication_mode_customerdetails')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customerdetails_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Customerdetails_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)


class Jobcard(models.Model):
    """Details of Jobcard Entity"""
    jobcard_no= models.CharField(max_length=50,blank=True, null=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customerid', default=1)
    order_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobcard_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobcard_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)


class Jobcard_Product(models.Model):
    """docstring for Jobcard_Product"""

    product_no= models.CharField(max_length=50,blank=True, null=True)
    productcard = models.CharField(max_length=100)
    jobcardid = models.ForeignKey(Jobcard, on_delete=models.CASCADE, related_name='jobcardid', default=1)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='paperid', default=1)
    gsm = models.ForeignKey(Gsm, on_delete=models.CASCADE, related_name='gsmid', default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='sizeid', default=1)
    size_custom = models.CharField(max_length=50,blank=True, null=True)
    squareinch = models.CharField(max_length=50,blank=True, null=True)
    quantity = models.CharField(max_length=50,blank=True, null=True)
    partialdelivery = models.CharField(max_length=50,blank=True, null=True)
    partial_qty = models.CharField(max_length=50,blank=True, null=True)
    partial_datetime= models.CharField(max_length=50,blank=True, null=True)
    side = models.CharField(max_length=50,blank=True, null=True)
    delivery_mode = models.CharField(max_length=50,blank=True, null=True)
    delivery_desc = models.CharField(max_length=250,blank=True, null=True)
    delivery_datetime = models.CharField(max_length=50,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Jobcard_Product_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Jobcard_Product_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Jobcard_Product_Process(models.Model):
    """Details of Jobcard_Product_Process Entity"""
    jobcard_productid= models.ForeignKey(Jobcard_Product, on_delete=models.CASCADE, related_name='jobcardproductid', default=1)
    processid = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='jobcardprocessid', default=1)
    datetime = models.DateTimeField(blank=True, null=True)
    jobtype = models.IntegerField(default=0)    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobcard_Product_Process_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobcard_Product_Process_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Series(models.Model):
    
    series_prefix=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE, default=1)
    series_count=models.IntegerField(default=0)
    series_for=models.CharField(max_length=50)
    is_default=models.BooleanField(default=True)


class Processcard(models.Model):
    """Details of Processcard Entity"""
    jobcardid = models.ForeignKey(Jobcard, on_delete=models.CASCADE, related_name='jobcard_id')
    jobcard_productno= models.CharField(max_length=50,blank=True, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    processid = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='process_id')
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_id',blank=True, null=True)
    assigned_to= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    machine=models.IntegerField(default=0)
    supplierid=models.IntegerField(default=0)
    del_datetime = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Processcard_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Processcard_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Comments(models.Model):
    
    comment=models.CharField(max_length=200,blank=True, null=True)
    file=models.FileField(max_length=200,blank=True, null=True)
    ref_id=models.ForeignKey(Processcard, on_delete=models.CASCADE, related_name='Processcard_id', default=1)
    ref_type=models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

class Role(models.Model):
    name= models.CharField(max_length=150, blank=True,null=True)
    
    size_create = models.IntegerField(default=0)
    size_update = models.IntegerField(default=0)
    size_delete = models.IntegerField(default=0)
    size_list = models.IntegerField(default=0)
    size_view = models.IntegerField(default=0)

    gsm_create = models.IntegerField(default=0)
    gsm_update = models.IntegerField(default=0)
    gsm_delete = models.IntegerField(default=0)
    gsm_list = models.IntegerField(default=0)
    gsm_view = models.IntegerField(default=0)

    paper_create = models.IntegerField(default=0)
    paper_update = models.IntegerField(default=0)
    paper_delete = models.IntegerField(default=0)
    paper_list = models.IntegerField(default=0)
    paper_view = models.IntegerField(default=0)

    process_create = models.IntegerField(default=0)
    process_update = models.IntegerField(default=0)
    process_delete = models.IntegerField(default=0)
    process_list = models.IntegerField(default=0)
    process_view = models.IntegerField(default=0)

    product_create = models.IntegerField(default=0)
    product_update = models.IntegerField(default=0)
    product_delete = models.IntegerField(default=0)
    product_list = models.IntegerField(default=0)
    product_view = models.IntegerField(default=0)

    delivery_create = models.IntegerField(default=0)
    delivery_update = models.IntegerField(default=0)
    delivery_delete = models.IntegerField(default=0)
    delivery_list = models.IntegerField(default=0)
    delivery_view = models.IntegerField(default=0)

    communication_create = models.IntegerField(default=0)
    communication_update = models.IntegerField(default=0)
    communication_delete = models.IntegerField(default=0)
    communication_list = models.IntegerField(default=0)
    communication_view = models.IntegerField(default=0)

    company_create = models.IntegerField(default=0)
    company_update = models.IntegerField(default=0)
    company_delete = models.IntegerField(default=0)
    company_list = models.IntegerField(default=0)
    company_view = models.IntegerField(default=0)


    jobcard_create = models.IntegerField(default=0)
    jobcard_update = models.IntegerField(default=0)
    jobcard_delete = models.IntegerField(default=0)
    jobcard_list = models.IntegerField(default=0)
    jobcard_view = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Role_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Role_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("name"),
        ]

class Employee(models.Model):
    """Details of Emploee Entity"""
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='empname', default=1)
    emp_id = models.CharField(max_length=50)
    role_type = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='Roletype', default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Roletype_Created_By_User', default=1)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Roletype_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("emp_id"),
        ]



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.ForeignKey(Role,on_delete=models.CASCADE, related_name='Permission_User',blank=True, null=True)
    deleted = models.BooleanField(default=False)
