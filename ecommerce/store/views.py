from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Order

def user_login(request):
    if request.method == 'POST':
username = request.POST.get('username')
password = request.POST.get('password')
user = authenticate(request, username=username, password=password)
if user is not None:
    login(request, user)
    return redirect('product_list')
else:
    messages.error(request, 'Invalid username or password.')

return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
return render(request, 'store/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
request.user.cart.products.add(product)
messages.success(request, 'Product added to cart.')
return redirect('product_list')

@login_required
def view_cart(request):
    cart = request.user.cart
return render(request, 'store/cart.html', {'cart': cart})


@login_required
def place_order(request):
    cart = request.user.cart
total_price = sum(product.price for product in cart.products.all())
order = Order.objects.create(user=request.user, total_price=total_price)
order.products.set(cart.products.all())
cart.products.clear()
messages.success(request, 'Order placed successfully.')
return redirect('product_list')