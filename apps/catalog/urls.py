from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/<slug:main_category_slug>/', views.main_category_view, name='main_category_view'),
    path('<slug:brand_slug>/', views.brand_view, name='brand_view'),
    path('<slug:brand_slug>/<slug:category_slug>/', views.category_view, name='category_view'),
    path('<slug:brand_slug>/<slug:category_slug>/<slug:product_slug>/',
         views.product_view, name='product_view'),
]

