from django.urls import path
from . import views


app_name='products'
urlpatterns=[
    path('',views.home , name='home'),
    path('<slug:slug>/' , views.details , name='details'),
    path('categories/<slug:cslug>/' , views.home , name = 'categories'),
    path('categories/<slug:cslug>/<slug:bslug>/' , views.home , name = 'brand'),
]