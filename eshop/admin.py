from django.contrib import admin
from .models import Product, Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","brand","category","price","in_cart")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","product","quantity","date_of_purchase","status")

admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)