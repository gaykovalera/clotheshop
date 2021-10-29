import os
import uuid

from django.db import models
from django.urls import reverse

from catalog.validators import validate_product


class Brand(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    slug = models.SlugField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:brand_view', kwargs={'brand_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    slug = models.SlugField(max_length=32, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:category_view',
            kwargs={'brand_slug': self.brand.slug, 'category_slug': self.slug}
        )


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    # 99999.9
    price = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Цена')
    slug = models.SlugField(max_length=32, unique=True)

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    addon = models.ManyToManyField("Addon", blank=True)
    brand = models.ManyToManyField("Brand", blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_view',
            kwargs={'brand_slug': self.brand.slug, 'category_slug': self.category.slug,
                    'product_slug': self.slug}
        )


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='products',
        null=True,
        blank=True,
        validators=[validate_product]
    )

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Изображение для {self.product.name}'


class Addon(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Цена')
    slug = models.SlugField(max_length=32, unique=True)

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name










