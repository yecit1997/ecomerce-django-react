from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status

from .models import Product
from .serializers import ProductSerializer



"""Obtenemos todos los productos de la base de datos"""
@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



"""Obtenemos un producto especifico de la base de datos"""
@api_view(["GET"])
def get_product(request, name):
    product = Product.objects.get(name=name)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)



"""Procedemos con la creación de los productos, validando si el usuario que lo esta creando
tiene permisos de administrador"""
@api_view(['POST'])
def create_produc(request):
    # Validamos si el usuario que va crear el producto tienen permisos de administrador
    if request.user.is_staff:
        serializer = ProductSerializer(data=request.data)
        # Validamos si el serializer es valido
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
   
    
    
"""Procedemos a editar los productos, validando si el usuario que lo esta editando
tiene permisos de administrador"""
@api_view(['PUT'])
def edit_produc(request, pk):
    # Obtenemos un producto por medio de la PK
    product = Product.objects.get(pk=pk)
    # Validamos si el usuario que va editar el producto tienen permisos de administrador
    if request.user.is_staff:
        serializer = ProductSerializer(product, data=request.data)
        # Validamos si el serializer es valido
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
    
    

"""Procedemos a eliminar un producto, basandonos en la PK, verificamos si el usuario que va ha realizar
la eliminación tiene permisos de administrado"""   
@api_view(['DELETE'])
def delete_produc(request, pk):
    # Obtenemos un producto por medio de la PK
    product = Product.objects.get(pk=pk)
    # Validamos si el usuario que va eliminar el producto tienen permisos de administrador
    if request.user.is_staff:
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)