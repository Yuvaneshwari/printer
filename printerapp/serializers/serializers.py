from rest_framework import serializers
from printerapp.models import *

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class GsmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gsm
        fields = "__all__"

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdetails
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CustomergroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = "__all__"

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaster
        fields = "__all__"

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class DeliverymodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverymode
        fields = "__all__"


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = "__all__"

class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobtype
        fields = "__all__"

class PaperpricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paperpricing
        fields = "__all__"

class CustomerdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerdetails
        fields = "__all__"

class JobcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcard
        fields = "__all__"

class Jobcard_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcard_Product
        fields = "__all__"

class Jobcard_Product_ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcard_Product_Process
        fields = "__all__"


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"

class ProcesscardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processcard
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
