from django.http import JsonResponse
from .models import Spirit
from .serializers import SpiritSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from spirit import serializers


# @api_view(['GET', 'POST'])
# def drink_link(request, format=None):

#     if request.method =='GET':
#         spirits= Spirit.objects.all()
#         serializer = SpiritSerializers(spirits, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = SpiritSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def drink_details(request, id, format=None):
#     try:
#         spirit = Spirit.objects.get(pk=id)

#     except Spirit.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SpiritSerializers(spirit)
#         return Response(serializer.data)
        
#     elif request.method == 'PUT':
#         serializer = SpiritSerializers(spirit, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         spirit.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class SpiritViewSet(viewsets.ModelViewSet):
    queryset = Spirit.objects.all()
    serializer_class = SpiritSerializers






    
