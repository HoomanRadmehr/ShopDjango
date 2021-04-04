from django.db import models
from accounts.models import User
from products.models import Product ,Category , Brand
from django.core.validators import MinValueValidator , MaxValueValidator

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'order')
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey('Coupon' , on_delete = models.CASCADE , related_name = 'd_coupon' , blank = True , null = True)

    def __str__(self):
        return f'str({self.user}) - str({self.id})'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_price_with_coupon(self):
        coupon = self.coupon
        total_price_without_coupon = float(Order.get_total_price(self))
        total = (1-(coupon.discount/100)) * total_price_without_coupon
        return total #price_with_coupon
    

    class Meta:
        ordering = ['-created']


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='c_order' , null=True , blank=True)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE , related_name='b_order' , null=True , blank=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='p_order')
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    discount = models.IntegerField(validators=[MinValueValidator(0) , MaxValueValidator(100)])
    valid_from = models.DateField()
    valid_to = models.DateField()
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.code

    