from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import *

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
    myFilters = FilterOrder(request.GET,queryset=orders)
    orders=myFilters.qs
    context = {'customer':customer,'orders':orders,'totalorders':totalorders,'filters':myFilters}
    return render(request,'accounts/customer.html',context)


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=order.objects.none(),instance=customer)
    #forms=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        #form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset,'customer':customer}
    return render(request,'accounts/order_form.html',context)


def UpdateOrder(request,pk):
    orders=order.objects.get(id=pk)
    forms=OrderForm(instance=orders)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'forms':forms}
    return render(request,'accounts/order_form.html',context)



def deleteOrder(request,pk):
    orders=order.objects.get(id=pk)
    if request.method=='POST':
        orders.delete()
        return redirect('/')
    context={'orders':orders}
    return render(request,'accounts/delete.html',context)   


