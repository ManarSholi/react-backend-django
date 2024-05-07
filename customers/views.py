from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customers.serializers import CustomerSelializer
from customers.models import Customer


@api_view(['GET', 'POST'])
def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSelializer(data, many=True)
    return Response(data={'customers': serializer.data})

@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSelializer(data)
        return Response(data={'customer': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = CustomerSelializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'customer': serializer.data})
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
