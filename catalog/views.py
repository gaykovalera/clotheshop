from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product, Addon, Brand

from cart.forms import CartAddProductForm


def home(request):
    brands = Brand.objects.all()
    return render(
        request,
        'catalog/home.html',
        {"brands": brands}
    )


def brand_view(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    categories = Category.objects.filter(product__brand__slug=brand_slug).distinct()
    return render(
        request,
        'catalog/brand.html',
        {"brand": brand,
         "categories": categories}
    )


def category_view(request, brand_slug, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(category__slug=category_slug)
    return render(
        request,
        'catalog/categories.html',
        {"category": category,
         "brand": brand,
         "products": products}
    )


#Добавить типизацию + prefetch_related для картинок:


def product_view(request, brand_slug, category_slug, product_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    pro = get_object_or_404(Product, slug=product_slug)
    category = get_object_or_404(Category, slug=category_slug)
    product = Category.objects.prefetch_related("product_set").get(slug=category_slug)
    products = Product.objects.filter(slug=product_slug)
    cart_product_form = CartAddProductForm()
    return render(
        request, 'catalog/products1.html',
        {"pro": pro,
         "product": product,
         "products": products,
         "brand": brand,
         "category": category,
         'cart_product_form': cart_product_form}
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














