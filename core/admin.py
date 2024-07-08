from django.contrib import admin

from .models.Product import Product
from .models.Type_Product import TypeProduct
from .models.Order import Order
from .models.Order_Product import OrderItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class TypeProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(TypeProduct, TypeProductAdmin)
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available',
                    'created', 'update']
    list_filter = ['available', 'created', 'update']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]