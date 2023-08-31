from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Код купона'
    )
    valid_from = models.DateTimeField(verbose_name='Дата начал действия')
    valid_to = models.DateTimeField(verbose_name='Дата окончания действия')
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        help_text='Размер скидки (от 0 до 100 %)',
        verbose_name='Размер скидки'
    )
    active = models.BooleanField(verbose_name='Состояние активности')

    class Meta:
        verbose_name = 'Купоны'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.code
