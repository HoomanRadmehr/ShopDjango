from products.models import Product
from django.shortcuts import get_object_or_404


CART_SESSION_ID = 'cart'


class Cart():
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID]={}
        self.cart = cart

    def __iter__(self):
        product_ides = self.cart.keys()
        products = Product.objects.filter(id__in = product_ides)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']= product
            cart[str(product.id)]['category'] = product.category
            cart[str(product.id)]['brand'] = product.brand

        for item in cart.values():
            item['total_price'] = float(item['price'])*int(item['quantity'])
            yield item

    def add(self,product,quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':'0' , 'price':str(product.price)}
        self.cart[product_id]['quantity'] = quantity
        self.save()

    def remove(self , request ,  product):
        product_id = str(product.id)
        del self.cart[product_id]
        self.save()

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(float(item['price'])*int(item['quantity']) for item in self.cart.values())