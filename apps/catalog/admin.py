from django.contrib import admin

from . import models


class BrandImageInLine(admin.TabularInline):
    model = models.BrandImage
    extra = 0
    max_num = 3


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandImageInLine]


class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage
    extra = 0
    max_num = 3


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    inlines = [ProductImageInLine]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Addon)
class AddonAdmin(admin.ModelAdmin):
    pass

