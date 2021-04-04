from django.contrib import admin
from .models import Product , Category,Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' ,'brand', 'price' , 'available']
    list_filter = ['available' , 'created']
    list_editable = ['price' , 'available']
    prepopulated_fields = {'slug':['name']}
    actions = ['make_available']

    def make_available(self , request , queryset):
        rows = queryset.update(available=True)
        self.message_user(request , f'{rows} updated')
    make_available.short_description = 'Change selected to available'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category']
    prepopulated_fields = {'slug':['name']}

