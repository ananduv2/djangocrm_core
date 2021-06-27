from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    ORDERS=order.objects.all()
    CUSTOMERS=Customer.objects.all()
    
    totalcustomers=CUSTOMERS.count()
    totalorders=ORDERS.count()
    delivered=ORDERS.filter(status='Delivered').count()
    pendings=ORDERS.filter(status='Pending').count()
    
    context={'order':ORDERS, 'customers':CUSTOMERS,'totalorders':totalorders,'pendings':pendings,'delivered':delivered}
    
    return render(request,'accounts/dashboard.html',context)

def products(request):
    PRODUCTS=product.objects.all()
    return render(request,'accounts/products.html',{'products':PRODUCTS})

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    totalorders=orders.count()
    return render(request,'accounts/customer.html',{'customer':customer,'orders':orders,'totalorders':totalorders})
