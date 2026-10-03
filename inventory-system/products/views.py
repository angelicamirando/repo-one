from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def add_product(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        Product.objects.create(
            name=name,
            price=price,
            stock=stock
        )
        return redirect('home')
     return render (request,'add_product.html')