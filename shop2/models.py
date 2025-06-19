from django.db import models
from django.contrib.auth.models import AbstractUser

MAX_LENGTH = 255
# Таблица статусов заказа
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус заказа')
    code = models.CharField(max_length=20, unique=True, verbose_name='Код статуса')
    is_active = models.BooleanField(default=True, verbose_name='Активный статус')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'статус заказа'
        verbose_name_plural = 'статусы заказов'

# Таблица способов оплаты
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, verbose_name='Способ оплаты')
    code = models.CharField(max_length=20, unique=True, verbose_name='Код способа')
    is_active = models.BooleanField(default=True, verbose_name='Доступен')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'способ оплаты'
        verbose_name_plural = 'способы оплаты'

# Таблица категорий товаров
class Categories(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

# Таблица меню
class MenuItem(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    weight = models.PositiveIntegerField(verbose_name='Вес (г)')
    cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления (мин)')
    is_spicy = models.BooleanField(default=False, verbose_name='Острое')
    is_vegetarian = models.BooleanField(default=False, verbose_name='Вегетарианское')
    photo = models.ImageField(upload_to='menu_items/', verbose_name='Фото')
    is_available = models.BooleanField(default=True, verbose_name='Доступно')
    
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f"{self.name} - {self.price} руб."
    
    class Meta:
        verbose_name = 'позиция меню'
        verbose_name_plural = 'позиции меню'

# Таблица корзины
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Корзина {self.created_at}"
    
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

# Таблица элементов корзины
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, verbose_name='Корзина')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, verbose_name='Позиция меню')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    
    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"
    
    class Meta:
        verbose_name = 'элемент корзины'
        verbose_name_plural = 'элементы корзины'

# Таблица заказов
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая сумма')
    address = models.TextField(verbose_name='Адрес доставки')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='Способ оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    payment_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата оплаты')

    menu_item = models.ManyToManyField(MenuItem, through='OrderItem', verbose_name='Позиция меню')

    def __str__(self):
        return f"Заказ #{self.id} - {self.created_at}"
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

# Таблица элементов заказов
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, verbose_name='Позиция меню')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity} ({self.order.pk})"
    
    class Meta:
        verbose_name = 'элемент заказа'
        verbose_name_plural = 'элементы заказа'        
   