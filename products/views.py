from django.http import HttpResponse

from products.models import Products
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer


# Create your views here.
def showProducts(request):
    Products.objects.all()
    data=Products.objects.all()
    print(data)
    print(data[0].name)
    data[0].name='Xilomi'
    data[0].save()
    print(data[0].name)
    print(request.META)
    return HttpResponse('Hello World!')

@api_view(['GET'])
def get_allProducts(request):
    data=Products.objects.all()
    serializedProducts = ProductSerializer(data, many=True)
    return Response(serializedProducts.data)

@api_view(['GET'])
def get_product(request,product_id):
    try:
        data=Products.objects.get(id=product_id)
        serializedProducts = ProductSerializer(data)
        return Response(serializedProducts.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def insertProduct(request):
    try:
        data=request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createcategory(request):
    try:
        data=request.data
        serializer = ProductSerializer(data=data)
        print(serializer)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

