import json
import re
from typing import List
from django.shortcuts import render
from rest_framework import serializers
from django.utils import timezone
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializerr
from django.views.decorators.csrf import csrf_exempt
import pdb

@api_view(["GET"])
def ListCompany(req):
    company = models.Company.objects.all()
    serializers = serializerr.CompanySerializer(company, many=True)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})

@api_view(['GET'])
def DetailCompany(req, key):
    arr = []
    for x in models.Company.objects.all():
        arr.append(x.id)
    if key in arr:
        company = models.Company.objects.get(id = key)
        serializers = serializerr.CompanySerializer(company)
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
    else:
        return Response({'errorCode': 400,'messages': 'Not found ID', 'current_t': timezone.now(),"data": ""})


@api_view(['POST'])
def CreateCompany(req):
    if req.POST:
        post_data = req.POST

        company = models.Company()

        company.name = post_data.get('name')
        company.address = post_data.get('address')
        company.phone = post_data.get('phone')
        company.description = post_data.get('description')
        company.save()
        serializers = serializerr.CompanySerializer(company)
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
    else:
        return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})
    
@api_view(['POST'])
def UpdateCompany(req, key):
        arr = []
        for x in models.Company.objects.all():
            arr.append(x.id)
        if key in arr:
            company = models.Company.objects.get(id = key)
            post_data = req.POST

            company.name = post_data.get('name')
            company.address = post_data.get('address')
            company.phone = post_data.get('phone')
            company.description = post_data.get('description')
            company.save()
            serializers = serializerr.CompanySerializer(company)
            return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
        else:
            return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})

@api_view(['POST'])    
def DeleteCompany(req, key):
    arr = []
    for x in models.Company.objects.all():
            arr.append(x.id)
    if key in arr:
        company = models.Company.objects.get(id = key)
        company.delete()
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": ""})
    else:
        return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})

@api_view(['GET'])
def abc(req, key):
    arr = []
    for x in models.Company.objects.all():
        arr.append(x.id)
    if key in arr:
        company = models.Company.objects.get(id = key)
        print(type(company))
        # print(type(company.tag_product.all()))
        # product = list(company.tag_product.all())
        # print(dir(product))
        lst_product = models.Product.objects.filter(company_id=key)
        print(type(lst_product))

        lst = [serializerr.ProductSerializer(x).data for x in lst_product]
        # pdb.set_trace()
        serializers = serializerr.CompanySerializer(company)

        data_pro_Comp = [{
            'Cpmpany': serializers.data,
            'product': lst
        }]

        # seria = serializerr.ProductSerializer(lst_product, many=True)

        
        # lst_a = [serializerr.ProductSerializer(x).data for x in lst_product]
        
        # ser = [x.data for x in [serializerr.ProductSerializer(x) for x in lst_product]]
        
        

        
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": data_pro_Comp})
    else:
        return Response({'errorCode': 400,'messages': 'Not found ID', 'current_t': timezone.now(),"data": ""})

# ------------------

@api_view(['GET'])
def ListProduct(req):
    product = models.Product.objects.all()
    serializers = serializerr.ProductSerializer(product, many=True)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})


@api_view(['GET'])
def  DetailProduct(req, key):
    arr = []
    for x in models.Product.objects.all():
        arr.append(x.id)
    if key in arr:
        product = models.Product.objects.get(id = key)
        serializers = serializerr.ProductSerializer(product)
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
    else:
        return Response({'errorCode': 400,'messages': 'Not found ID', 'current_t': timezone.now(),"data": ""})


@api_view(['POST'])
def CreateProduct(req):
    if req.POST:
        post_data = req.POST

        product = models.Product()

        product.price = post_data.get('price')
        product.product_code = post_data.get('product_code')
        product.description = post_data.get('description')
        product.image = req.FILES['image']
        product.create_at = post_data.get('create_at')
        product.update_at = post_data.get('update_at')
        company = int(post_data.get('company'))
        product.company = models.Company.objects.get(id=company)
        product.save()
        serializers = serializerr.ProductSerializer(product)
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
    else:
        return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})

@api_view(['POST'])
def UpdateProduct(req, key):
        arr = []
        for x in models.Product.objects.all():
            arr.append(x.id)
        if key in arr:
            product = models.Product.objects.get(id = key)
            post_data = req.POST

            product.price = post_data.get('price')
            product.product_code = post_data.get('product_code')
            product.description = post_data.get('description')
            product.image = req.FILES['image']
            product.create_at = post_data.get('create_at')
            product.update_at = post_data.get('update_at')
            company = int(post_data.get('company'))
            product.company = models.Company.objects.get(id=company)
            product.save()
            serializers = serializerr.ProductSerializer(product)
            return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": serializers.data})
        else:
            return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})

@api_view(['POST'])    
def DeleteProduct(req, key):
    arr = []
    for x in models.Product.objects.all():
            arr.append(x.id)
    if key in arr:
        product = models.Product.objects.get(id = key)
        product.delete()
        return Response({'errorCode': 0,'messages': 'successfully', 'current_t': timezone.now(),"data": ""})
    else:
        return Response({'errorCode': 400,'messages': 'Not found data', 'current_t': timezone.now(),"data": ""})



    
    

    
    
    

