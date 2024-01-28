from django.http import JsonResponse, Http404
from customers.serializers import CustomerSelializer
from customers.models import Customer


def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSelializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        raise Http404('Customer does not exist')

    serializer = CustomerSelializer(data)
    return JsonResponse({'customer': serializer.data})
