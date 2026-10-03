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

def edit_product(request, product_id):
    product= Product.objects.get(id=product_id)

    if request.method=="POST":
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.stock=request.POST.get('stock')

        product.save()

        return redirect('home')

    return render(request, 'edit_product.html', {'product':product})

def delete_product(reqeust,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()

    return redirect('home')
