from django.shortcuts import render, redirect , get_object_or_404
from cart.cartsession import Cart
from . models import Order , OrderItem , Coupon
from .forms import CouponForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
from accounts.models import User

@login_required
def create_order(request): 
    cart = Cart(request)
    order = Order.objects.create(user = request.user)
    for item in cart:
        OrderItem.objects.create(order = order , category=item['category'] , brand= item['brand'] , product = item['product'] , price = item['price'] , quantity=item['quantity'])
        cart.clear()
        return redirect('orders:detail', order.id)

@login_required
def detail(request , order_id):
    order = get_object_or_404(Order , id = order_id)
    form = CouponForm()
    takhfif = False
    if order.coupon:
        takhfif = True
    return render (request , 'orders/detail.html' , context = {'order':order , 'form':form , 'takhfif':takhfif})

@require_POST
def coupon_apply(request , order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact = code , valid_from__lte = now , valid_to__gte = now , active = True)
        except Coupon.DoesNotExist:
            messages.error(request , 'Your coupon code does not exist' , 'danger')
            return redirect('orders:detail' , order_id)

        order = Order.objects.get(id = order_id)
        order.coupon = coupon
        order.save()
        return redirect ("orders:detail" , order.id)
    