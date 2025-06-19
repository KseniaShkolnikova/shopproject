from rest_framework import serializers
from shop2.models import *

class OrderStatusSer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

      #  [
       #     'name',
        #    'is_active'
        #]

class MenuItemSer(serializers.ModelSerializer):
    price = serializers.DecimalField(label = 'цена', max_digits=10, decimal_places=2)
    class Meta:
        model = MenuItem
        fields = '__all__'

class PaymentMethodSer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class CategoriesSer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class OrderSer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(label = 'цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'