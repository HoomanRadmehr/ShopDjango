from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:categories',args=[self.slug,])


class Brand(models.Model):
    category = models.ForeignKey(Category , on_delete = models.CASCADE , related_name='cbrand')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:brand' , args=[self.category.slug , self.slug])

    
class Product(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='Cproduct')
    brand = models.ForeignKey(Brand , on_delete= models.CASCADE , related_name = 'bproduct' , null=True , blank = True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.DecimalField(max_digits=7 , decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:details',args=([self.slug]))
