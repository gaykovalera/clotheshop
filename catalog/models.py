from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    slug = models.SlugField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    slug = models.SlugField(max_length=32, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


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


class Addon(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Цена')
    slug = models.SlugField(max_length=32, unique=True)

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name










