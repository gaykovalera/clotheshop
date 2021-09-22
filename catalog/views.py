from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product, Addon, Brand


def home(request):
    cat = Category.objects.all()
    return render(
        request,
        'catalog/home.html',
        {"categories": cat}
    )


def category_view(request, category_slug):
    cat = get_object_or_404(Category, slug=category_slug)
    return HttpResponse(cat.name)


def productname(request):
    pro = Product.objects.all()
    return render(
        request,
        'catalog/productname.html',
        {"product": pro}
    )


def product_view(request, product_slug):
    pro = get_object_or_404(Product, slug=product_slug)
    return HttpResponse(pro.name)


def products_view(request, category_slug):
    cat = Category.objects.prefetch_related("product_set").get(slug=category_slug)
    return render(
        request, 'catalog/home.html',
        {"category": cat}
    )


def add(request):
    on = Addon.objects.all()
    return render(
        request,
        'catalog/add.html',
        {"addon": on}
    )


def addon_view(request, addon_slug):
    on = get_object_or_404(Addon, slug=addon_slug)
    return HttpResponse(on.name)


def brand_name(request):
    br = Brand.objects.all()
    return render(
        request,
        'catalog/brand.html',
        {"brand": br}
    )


def brand_view(request, brand_slug):
    br = get_object_or_404(Brand, slug=brand_slug)
    return HttpResponse(br.name)










