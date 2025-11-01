from django.shortcuts import render, redirect
from .models import Product, Order, CATEGORY_CHOICES
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Min, Max
# Create your views here.
@login_required(login_url="/auth/login/")
def home(request):
    products = Product.objects.all()
    selected_category = request.GET.get("category", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    if selected_category and selected_category != "all":
        products = products.filter(category=selected_category)

    try:
        if min_price:
            min_price_value = int(min_price)
            products = products.filter(price__gte=min_price_value)
    except ValueError:
        min_price = ""

    try:
        if max_price:
            max_price_value = int(max_price)
            products = products.filter(price__lte=max_price_value)
    except ValueError:
        max_price = ""

    price_bounds = Product.objects.aggregate(min_price=Min("price"), max_price=Max("price"))

    context = {
        "products": products,
        "category_choices": CATEGORY_CHOICES,
        "selected_category": selected_category,
        "min_price": min_price,
        "max_price": max_price,
        "price_bounds": price_bounds,
    }
    return render(request,"eshop/home.html",context=context)

@login_required(login_url="/auth/login/")
def product_info(request,data):
    if request.method == "POST":
        product_id = request.POST.get("pid")
        if 'add_to_cart' in request.POST:
            product = Product.objects.get(id=product_id)
            product.in_cart= True
            product.save()
            return redirect('cart')
    product = Product.objects.get(id=data)
    context = {
        "product":product
    }
    return render(request,"eshop/product_info.html",context=context)

@csrf_exempt
@login_required(login_url="/auth/login/")
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        print('got',product_id)
        product = Product.objects.get(id=product_id)
        product.in_cart = True
        product.save()
        
        return HttpResponse(product_id)

@csrf_exempt
@login_required(login_url="/auth/login/")
def checkout(request):
    if request.method == "POST":
        quantity = request.POST.getlist('quantity[]')
        quantity = [int(i) for i in quantity]
        print(quantity)
        products = Product.objects.filter(in_cart=True)
        for i,product in enumerate(products):
            product.in_cart=False
            product.save()
            order = Order.objects.create(product=product,customer=request.user,quantity=quantity[i])
            order.save()

        return HttpResponse(products)

@login_required(login_url="/auth/login/")
def cart(request):
    if request.method == "POST":
        product_id = request.POST.get("pid")
        if 'remove' in request.POST:
            product = Product.objects.get(id=product_id)
            product.in_cart = False
            product.save() 
            return redirect('cart')
        
    products = Product.objects.filter(in_cart=True)
    cart_total = 0
    for product in products:
        cart_total += product.price

    context = {
        "products":products,
        "cart_total":cart_total
    }
    return render(request,"eshop/cart.html",context=context)

@login_required(login_url="/auth/login/")
def orders(request):   
    if request.method == "POST":
        order_id = request.POST.get("oid")
        if 'cancel' in request.POST:
            order = Order.objects.get(id=order_id)
            order.delete()
    orders = Order.objects.filter(customer=request.user)
    context = {
        "orders":orders
    } 
    return render(request,"eshop/orders.html",context=context)

