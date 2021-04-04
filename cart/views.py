from django.shortcuts import render , get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .forms import AddCartForm
from .cartsession import Cart
from django.contrib import messages

def detail(request):
    cart = Cart(request)
    return render(request,'cart/detail.html' , context={'cart':cart})

@require_POST
def add_cart(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = AddCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product , quantity = cd['quantity'])
        return redirect ('cart:detail')
        
def remove_cart(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id = product_id)
    cart.remove(request , product)
    messages.success(request , 'Your product deleted from your cart successfully','success')
    return redirect ('cart:detail')
    