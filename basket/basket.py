from django.conf import settings
from shop2.models import MenuItem

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        product_ids = self.basket.keys()
        products = MenuItem.objects.filter(pk__in=product_ids)
        
        basket_copy = self.basket.copy()  
        
        for product in products:
            product_id = str(product.pk)
            if product_id in basket_copy:
                basket_copy[product_id]['product'] = product
                basket_copy[product_id]['total_price'] = float(basket_copy[product_id]['price']) * int(basket_copy[product_id]['quantity'])
        
        for item in basket_copy.values():
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())
    
    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        return sum(float(item['price']) * int(item['quantity']) for item in self.basket.values())
    
    def clear(self):
        if settings.BASKET_SESSION_ID in self.session:
            del self.session[settings.BASKET_SESSION_ID]
            self.session.modified = True