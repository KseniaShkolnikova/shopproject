from django.contrib import admin
from .models import *

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

