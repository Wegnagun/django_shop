from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """ Модель категорий товаров. """
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование категории'
    )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Модель товаров. """
    category = models.ForeignKey(
        Category,
        related_name='product',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='product/%Y/%m/%d',
        blank=True,
        verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.1,
                message='Цена не может быть меньше 0.1!'
            ),
        ]
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
