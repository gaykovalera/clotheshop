from django.shortcuts import render, get_object_or_404

from apps.catalog.models import Category, MainCategory, Product, Brand

from apps.cart.forms import CartAddProductForm


def home(request):
    brands = Brand.objects.all()
    return render(
        request,
        'catalog/home.html',
        {"brands": brands}
    )


def brand_view(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    categories = Category.objects.prefetch_related('product_set').filter(product__brand__slug=brand_slug).distinct()
    products = Product.objects.filter(brand__slug=brand_slug)
    return render(
        request,
        'catalog/brand.html',
        {"brand": brand,
         "categories": categories,
         "products": products}
    )


def main_category_view(request, main_category_slug):
    main_category = get_object_or_404(MainCategory, slug=main_category_slug)
    products = Product.objects.filter(category__main_category__slug=main_category_slug)
    return render(
        request,
        'catalog/main_cat.html',
        {"products": products,
         "main_category": main_category}
    )


def category_view(request, brand_slug, category_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)
    return render(
        request,
        'catalog/categories.html',
        {"category": category,
         "brand": brand,
         "products": products}
    )


def product_view(request, brand_slug, category_slug, product_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    pro = get_object_or_404(Product, slug=product_slug)
    category = get_object_or_404(Category, slug=category_slug)
    product = Category.objects.prefetch_related('product_set').filter(product__brand__slug=brand_slug).distinct()
    products = Product.objects.filter(slug=product_slug)
    image = Product.objects.prefetch_related("productimage_set")
    cart_product_form = CartAddProductForm()
    return render(
        request, 'catalog/products1.html',
        {"pro": pro,
         "product": product,
         "products": products,
         "brand": brand,
         "category": category,
         "image": image,
         'cart_product_form': cart_product_form}
    )

















