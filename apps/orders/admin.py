from django.contrib import admin
from .models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = list_display


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_feature')
    list_display_links = list_display