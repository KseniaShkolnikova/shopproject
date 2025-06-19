from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from shop2.models import *
from .permission import *
from rest_framework import mixins
from rest_framework.renderers import AdminRenderer

class OrderStatusViewSer (#mixins.ListModelMixin, 
                          #mixins.RetrieveModelMixin, 
                          #mixins.CreateModelMixin, 
                          #mixins.UpdateModelMixin, 
                          #mixins.DestroyModelMixin, 
                          #viewsets.GenericViewSet
                          viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage

    def get_queryset(self):
        queryset = OrderStatus.objects.all()
        name = self.request.query_params.get('name', None)
        code = self.request.query_params.get('code', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif code is not None:
            queryset = queryset.filter(code__icontains=code)

        return queryset



class OrderViewSer (viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage
    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get('status', None)
        payment_method = self.request.query_params.get('payment_method', None)

        if status is not None:
            queryset = queryset.filter(status__icontains=status)
        elif payment_method is not None:
            queryset = queryset.filter(payment_method__icontains=payment_method)

        return queryset

class OrderItemViewSer (viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage

    def get_queryset(self):
        queryset = OrderItem.objects.all()
        menu_item = self.request.query_params.get('menu_item', None)
        order = self.request.query_params.get('order', None)

        if menu_item is not None:
            queryset = queryset.filter(menu_item__name__icontains=menu_item)
        elif order is not None:
            queryset = queryset.filter(order__id__icontains=order)

        return queryset

class MenuItemViewSer (viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset

class CategoriesViewSer (viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage
    def get_queryset(self):
        queryset = Categories.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset

class PaymentMethodViewSer (viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSer
    permission_classes =[CustomPermission]
    pagination_class = PagenationPage
    def get_queryset(self):
        queryset = Categories.objects.all()
        name = self.request.query_params.get('name', None)
        code = self.request.query_params.get('code', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif code is not None:
            queryset = queryset.filter(code__icontains=code)

        return queryset
