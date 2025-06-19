from django.urls import path, include
from .views import *

app_name = 'basket' 

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('clear/', basket_clear, name='basket_clear'),
    path('buy/', basket_buy, name='basket_buy'),
    
]