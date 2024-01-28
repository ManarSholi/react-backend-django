from django.http import JsonResponse
from customers.serializers import CustomerSelializer
from customers.models import Customer


def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSelializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

def customer(request, id):
    data = Customer.objects.get(pk=id)
    serializer = CustomerSelializer(data)
    return JsonResponse({'customer': serializer.data})
