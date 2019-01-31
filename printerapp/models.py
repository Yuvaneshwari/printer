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
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Process_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Process_Modified_By_User', default=1)
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


class Role(models.Model):
    """Details of Role Entity"""
    role_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Role_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Role_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("role_name"),
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

class Customer(models.Model):
    """docstring for Customer"""
    name = models.CharField(max_length=100)
    customergroup = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    primary_contact_no = models.CharField(max_length=50)
    email_id = models.EmailField(blank=True, null=True)
    contact_person = models.CharField(max_length=50,blank=True, null=True)
    contact_person_contact_no = models.CharField(max_length=50,blank=True, null=True)
    contact_person_email_id = models.EmailField(max_length=50,blank=True, null=True)
    secondary_contact_no = models.CharField(max_length=50,blank=True, null=True)
    secondary_email_id = models.EmailField(blank=True, null=True)
    referred_by = models.IntegerField(default=False)
    address = models.CharField(max_length=200)
    state= models.ForeignKey(StateMaster, on_delete=models.CASCADE, related_name='customer_State')
    max_credit_amount = models.IntegerField(default=0)
    credit_days = models.IntegerField(default=0)
    credit_status = models.CharField(max_length=30)
    billing_address = models.CharField(max_length=200)
    shiping_address = models.CharField(max_length=200)
    gst_no = models.CharField(max_length=20,blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    default_cash_customer=models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Customer_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Customer_Modified_By_User', default=1)
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