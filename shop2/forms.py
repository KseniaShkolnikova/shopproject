from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name','description','price','weight','cooking_time','is_spicy',
                  'is_vegetarian','photo','is_available','category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_spicy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_vegetarian': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['description','photo','name']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }



class OrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Покупатель",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Order
        fields = ['user', 'status', 'address', 'comment', 'payment_method']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all().order_by('username')
        
        # Для нового заказа устанавливаем статус по умолчанию
        if not self.instance.pk:
            self.fields['status'].initial = OrderStatus.objects.get(code='new')

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order','menu_item','quantity']  
        widgets = {
            'order': forms.Select(attrs={'class': 'form-select'}),
            'menu_item': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=2,
        help_text=''
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm (AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        min_length=2
    )        
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )  
    class Meta:
        model = User
        fields = ['username','email','password','password2']
