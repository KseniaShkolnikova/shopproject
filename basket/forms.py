from django import forms
from shop2.models import Order, OrderStatus, PaymentMethod
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class BasketAddProductForm (forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20,initial=1, label='количество',
                 widget=forms.NumberInput(attrs={'class':'form-control'}))
    reload = forms.BooleanField(required=False, initial=False, widget = forms.HiddenInput)                      

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['comment', 'address', 'payment_method', 'status', 'total_price']
        widgets = {
            'status': forms.HiddenInput(),
            'total_price': forms.HiddenInput(),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
