from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product, Addon, Brand


def home(request):
    br = Brand.objects.all()
    return render(
        request,
        'catalog/home.html',
        {"brands": br}
    )


def brand_view(request, brand_slug):
    br = get_object_or_404(Brand, slug=brand_slug)
    cats = Category.objects.filter(product__brand__slug=brand_slug)
    return render(
        request,
        'catalog/brand.html',
        {"brand": br,
         "categories": cats}
    )


def category_view(request, brand_slug, category_slug):
    cat = get_object_or_404(Category, slug=category_slug)
    br = get_object_or_404(Brand, slug=brand_slug)
    pro = Product.objects.filter(category__slug=category_slug)
    return render(
        request,
        'catalog/categories.html',
        {"category": cat,
         "brand": br,
         "products": pro}
    )


def product_view(request, brand_slug, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cat = Category.objects.prefetch_related("product_set").get(slug=category_slug)
    return render(
        request, 'catalog/products1.html',
        {"product": product,
         "category": cat}
    )


def addon_view(request, brand_slug, category_slug, product_slug, addon_slug):
    on = get_object_or_404(Addon, slug=addon_slug)
    ad = Addon.objects.filter(Addon, slug=addon_slug)
    return render(
        request,
        'catalog/add.html',
        {"addon": on,
         "addons": ad}
    )














