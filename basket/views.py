from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .basket import Basket
from basket.forms import *
from shop2.models import *

def basket_detail(request):
    basket = Basket(request)
    for item in basket:
        if not hasattr(item['product'], 'id'):
            print(f"Найден товар без ID: {item}")
            basket.remove(item['product'])
    return render(request, 'basket/basket_detail.html', {'basket': basket})

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(MenuItem, pk=product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')

def basket_clear (request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket:basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(MenuItem, pk=product_id)
    form = BasketAddProductForm(request.POST)
    
    if form.is_valid():
        basket.add(
            product=product,
            quantity=form.cleaned_data['quantity'],
            update_quantity=form.cleaned_data['reload'] 
        )
    return redirect('basket:basket_detail')
@login_required
def basket_buy(request):
    basket = Basket(request)
    
    if not basket:
        return redirect('basket:basket_detail')

    status, created = OrderStatus.objects.get_or_create(
        code='new',
        defaults={'name': 'Новый', 'is_active': True}
    )
    
    payment_method = PaymentMethod.objects.filter(is_active=True).first()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = basket.get_total_price()
            order.status = status
            order.save()
            
            for item in basket:
                OrderItem.objects.create(
                    menu_item=item['product'],
                    quantity=item['quantity'],
                    order=order
                )
            basket.clear()
            return redirect('basket:basket_detail')
    else:
        initial_data = {
            'status': status.id,
            'payment_method': payment_method.id if payment_method else None,
            'total_price': basket.get_total_price()
        }
        form = OrderForm(initial=initial_data)
    
    return render(request, 'orders/order_form.html', {'form': form, 'basket': basket})

@login_required
def open_order(request):
    return redirect('basket_buy')