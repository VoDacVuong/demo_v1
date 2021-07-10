from rest_framework import fields, serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Company
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = models.Product
        fields = '__all__'
