from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model representing a category."""

    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Идентификатор')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Model representing a product."""

    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Идентификатор')
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    available = models.BooleanField(default=True, verbose_name='Наличие ')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикаций'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
