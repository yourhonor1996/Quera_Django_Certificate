from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['POST'])
def create_product(request):
    name = request.data.get('name')
    price = request.data.get('price')
    new_product = Product(name= name, price= price)
    new_product.save()
    
    return Response({
        "message": "new product added successfully",
        "product": {
            "name": name,
            "price": price
            }
        }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product(request, product_id):
    product = Product.objects.get(id = product_id)
    return Response({
        'name': product.name,
        'price': product.price
    }, status=status.HTTP_200_OK)
