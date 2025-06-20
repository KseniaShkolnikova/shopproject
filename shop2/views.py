from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime, timezone


class OrderItemListView(PermissionRequiredMixin,ListView):
    permission_required = 'shop.view_orderItem'
    model = OrderItem
    template_name = 'OrderItem/OrderItem_list.html'
    context_object_name = 'OrderItem'
    
class OrderItemDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'shop.view_orderItem'
    model = OrderItem
    template_name = 'OrderItem/OrderItem_detail.html'
    context_object_name = 'OrderItem'    

class OrderItemCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'shop.add_orderItem'
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'OrderItem/OrderItem_form.html'
    success_url= reverse_lazy('OrderItem_list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.order.calculate_total()  
        return response

class OrderItemUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'shop.change_orderItem'
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'OrderItem/OrderItem_form.html'
    success_url= reverse_lazy('OrderItem_list_view')    

class OrderItemdeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'shop.delete_orderItem'
    model = OrderItem
    context_object_name = 'OrderItem'    
    template_name = 'OrderItem/OrderItem_confirm_delete.html'
    success_url= reverse_lazy('OrderItem_list_view') 



class OrderListView(PermissionRequiredMixin,ListView):
    permission_required = 'shop.view_order'
    model = Order
    template_name = 'Order/Order_list.html'
    context_object_name = 'Order'
    
class OrderDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'shop.view_order'
    model = Order
    template_name = 'Order/Order_detail.html'
    context_object_name = 'Order'    
    queryset = Order.objects.prefetch_related('orderitem_set__menu_item')
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        self.object.calculate_total()  
        self.object.save()  
        return response

from django.utils import timezone

class OrderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_order'
    model = Order
    form_class = OrderForm
    template_name = 'Order/Order_form.html'
    success_url = reverse_lazy('Order_list_view')

    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.status = OrderStatus.objects.get(code='new')
        
        response = super().form_valid(form)
        self.object.calculate_total()
        return response


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_order'
    model = Order
    form_class = OrderForm
    template_name = 'Order/Order_form.html'
    success_url = reverse_lazy('Order_list_view')

    def form_valid(self, form):
        old_status = self.object.status
        
        response = super().form_valid(form)
        
        if self.object.status.code == '3' and old_status.code != '3':
            self.object.is_paid = True
            self.object.payment_date = timezone.now() 
            self.object.save()
        
        self.object.calculate_total()
        
        return response

class OrderdeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'shop.delete_order'
    model = Order
    context_object_name = 'Order'    
    template_name = 'Order/Order_confirm_delete.html'
    success_url= reverse_lazy('Order_list_view') 




class CategoriesListView(PermissionRequiredMixin,ListView):
    permission_required = 'shop.view_categories'
    model = Categories
    template_name = 'Categories/Categories_list.html'
    context_object_name = 'Categories'
    
class CategoriesDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'shop.view_categories'
    model = Categories
    template_name = 'Categories/Categories_detail.html'
    context_object_name = 'Categories'    

class CategoriesCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'shop.add_categories'
    model = Categories
    form_class = CategoriesForm
    template_name = 'Categories/Categories_form.html'
    success_url= reverse_lazy('Categories_list_view')

class CategoriesUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'shop.change_categories'
    model = Categories
    form_class = CategoriesForm
    template_name = 'Categories/Categories_form.html'
    success_url= reverse_lazy('Categories_list_view')    

class CategoriesdeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'shop.delete_categories'
    model = Categories
    context_object_name = 'Categories'    
    template_name = 'Categories/Categories_confirm_delete.html'
    success_url= reverse_lazy('Categories_list_view') 





class MenuItemListView(PermissionRequiredMixin,ListView):
    permission_required = 'shop.view_menuItem'
    model = MenuItem
    template_name = 'MenuItem/MenuItem_list.html'
    context_object_name = 'MenuItem'
    
class MenuItemDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'shop.view_menuItem'
    model = MenuItem
    template_name = 'MenuItem/MenuItem_detail.html'
    context_object_name = 'MenuItem'    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form_basket'] =BasketAddProductForm()
        return context
        

class MenuItemCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'shop.add_menuItem'
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'MenuItem/MenuItem_form.html'
    success_url= reverse_lazy('MenuItem_list_view')

class MenuItemUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'shop.change_menuItem'
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'MenuItem/MenuItem_form.html'
    success_url= reverse_lazy('MenuItem_list_view')    

class MenuItemdeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'shop.delete_menuItem'
    model = MenuItem
    context_object_name = 'MenuItem'    
    template_name = 'MenuItem/MenuItem_confirm_delete.html'
    success_url= reverse_lazy('MenuItem_list_view') 

# Create your views here.
def main_view (request):
    return render (request, 'main.html')

def about_view (request):
    return render (request, 'about.html')

def cart_view (request):
    return render (request, 'cart.html')

def products_view (request):
    return render (request, 'products.html')

def electonica_view (request):
    return render (request, 'products.html')

def all_view (request):
    return render (request, 'products.html')

def children_view (request):
    return render (request, 'products.html')

def health_view (request):
    return render (request, 'products.html')

def sport_view (request):
    return render (request, 'products.html')

def for_home_view (request):
    return render (request, 'products.html')

def clother_view (request):
    return render (request, 'products.html')

def tehnica_view (request):
    return render (request, 'products.html')

def products_view(request):
    category_id = request.GET.get('category')
    categories = Categories.objects.all()
    
    menu_items = MenuItem.objects.filter(is_available=True)
    current_category = None
    
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
        current_category = int(category_id)
    
    return render(request, 'products.html', {
        'menu_items': menu_items,
        'categories': categories,
        'current_category': current_category,
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products')
    else:
        form = LoginForm()
    return render(request,'Auth/Login.html', context={'form':form})  


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products')
    else:
        form = RegistrationForm()
    return render(request,'Auth/Registration.html', context={'form':form}) 

def logout_user(request):
    logout(request)
    return redirect('products')
