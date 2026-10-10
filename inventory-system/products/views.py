from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Sum


def home(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
        total_products = Product.objects.count()
        total_stock = Product.objects.aggregate(Sum('stock'))['stock__sum'] or 0
    return render(request, 'home.html',  {'products': products,
        'total_products': total_products,
        'total_stock': total_stock,})


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
