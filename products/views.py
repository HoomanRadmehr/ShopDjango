from django.shortcuts import render , get_object_or_404
from . models import Product , Category , Brand
from cart.forms import AddCartForm
from . forms import PriceFilter

def home(request , cslug = None , bslug = None):
    if request.method=="POST":
        form = PriceFilter(request.POST)
        if form.is_valid():
            minimum = form.cleaned_data['min']
            maximum = form.cleaned_data['max']
            products = Product.objects.filter(price__gte = minimum , price__lte = maximum , available = True)
    else:
        products = Product.objects.filter(available = True)
        form = PriceFilter()

    categories = Category.objects.all()
    brands = Brand.objects.all()

    if bslug is not None:
        category = get_object_or_404(Category,slug=cslug)
        brand = get_object_or_404(Brand,slug=bslug)
        products = Product.objects.filter(category = category , brand = brand , available = True)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        return render (request , 'products/home.html' , context={'products':products , 'categories':categories , 'brands':brands})

    elif cslug is not None:
        category = get_object_or_404(Category,slug=cslug)
        products = Product.objects.filter(category= category , available = True)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        return render (request , 'products/home.html' , context={'products':products , 'categories':categories , 'brands':brands})
    else:
        return render (request , 'products/home.html' , context={'products':products , 'categories':categories , 'brands':brands , 'form':form})    

def details(request , slug):
    product = get_object_or_404(Product , slug = slug)
    form = AddCartForm()
    return render(request,'products/details.html' , {'product':product , 'form':form})
    