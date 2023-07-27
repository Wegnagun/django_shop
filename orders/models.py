from django.conf import settings
from django.db import models

from shop.models import Product


class Order(models.Model):
    """ Модель заказов. """
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=250, verbose_name='Улица')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый код')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    stripe_id = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Идентификатор платежа'
    )

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        path = '/'
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
    """ Модель регистрации заказов. """
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Товары в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
