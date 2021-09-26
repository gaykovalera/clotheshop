from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:brand_slug>/', views.brand_view, name='brand_view'),
    path('<slug:brand_slug>/<slug:category_slug>/', views.category_view, name='category_view'),
    path('<slug:brand_slug>/<slug:category_slug>/<slug:product_slug>/', views.product_view, name='product_view'),
    path('<slug:addon_slug>/', views.addon_view, name='addon_view'),
]

