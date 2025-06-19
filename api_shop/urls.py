from rest_framework import routers
from .views import *


urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register('menuItem', MenuItemViewSer, basename='menuItem')
router.register('OrderItem', OrderItemViewSer, basename='OrderItem')
router.register('Categories', CategoriesViewSer, basename='Categories')
router.register('OrderStatus', OrderStatusViewSer, basename='OrderStatus')
router.register('Order', OrderViewSer, basename='Order')
router.register('PaymentMethod', PaymentMethodViewSer, basename='PaymentMethod')
urlpatterns +=router.urls