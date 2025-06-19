from django.contrib import admin
from django.urls import path, include
from .views import *
from basket.views import *

urlpatterns = [
    path('', main_view,name='main'),

    path('about/',about_view,name='about'),
    path('basket/bye/',basket_detail,name='basket_detail'),
    path('products/',products_view,name='products'),
    path('products/all',all_view,name='all'),

    path('OrderItem/', OrderItemListView.as_view(), name = 'OrderItem_list_view' ),
    path('OrderItem/<int:pk>', OrderItemDetailView.as_view(), name='OrderItem_detail_view'),
    path('OrderItem/create/', OrderItemCreateView.as_view(), name='OrderItem_create_view'),
    path('OrderItem/<int:pk>/update/', OrderItemUpdateView.as_view(), name='OrderItem_update_view'),
    path('OrderItem/<int:pk>/delete/', OrderItemdeleteView.as_view(), name='OrderItem_delete_view'),

    path('CartItem/', CartItemListView.as_view(), name = 'CartItem_list_view' ),
    path('CartItem/<int:pk>', CartItemDetailView.as_view(), name='CartItem_detail_view'),
    path('CartItem/create/', CartItemCreateView.as_view(), name='CartItem_create_view'),
    path('CartItem/<int:pk>/update/', CartItemUpdateView.as_view(), name='CartItem_update_view'),
    path('CartItem/<int:pk>/delete/', CartItemdeleteView.as_view(), name='CartItem_delete_view'),

    path('Categories/', CategoriesListView.as_view(), name = 'Categories_list_view' ),
    path('Categories/<int:pk>', CategoriesDetailView.as_view(), name='Categories_detail_view'),
    path('Categories/create/', CategoriesCreateView.as_view(), name='Categories_create_view'),
    path('Categories/<int:pk>/update/', CategoriesUpdateView.as_view(), name='Categories_update_view'),
    path('Categories/<int:pk>/delete/', CategoriesdeleteView.as_view(), name='Categories_delete_view'),

    path('MenuItem/', MenuItemListView.as_view(), name = 'MenuItem_list_view' ),
    path('MenuItem/<int:pk>', MenuItemDetailView.as_view(), name='MenuItem_detail_view'),
    path('MenuItem/create/', MenuItemCreateView.as_view(), name='MenuItem_create_view'),
    path('MenuItem/<int:pk>/update/', MenuItemUpdateView.as_view(), name='MenuItem_update_view'),
    path('MenuItem/<int:pk>/delete/', MenuItemdeleteView.as_view(), name='MenuItem_delete_view'),

    path('Order/',OrderListView.as_view(), name = 'Order_list_view' ),
    path('Order/<int:pk>',OrderDetailView.as_view(), name='Order_detail_view'),
    path('Order/create/',OrderCreateView.as_view(), name='Order_create_view'),
    path('Order/<int:pk>/update/',OrderUpdateView.as_view(), name='Order_update_view'),
    path('Order/<int:pk>/delete/',OrderdeleteView.as_view(), name='Order_delete_view'),

    path('login/',login_user, name = 'login_user' ),
    path('registration/',registration_user, name = 'registration_user' ),
    path('logout/',logout_user, name = 'logout_user' ),
]
