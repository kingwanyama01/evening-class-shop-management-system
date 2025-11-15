from django.urls import path
from . import views as products_views

urlpatterns = [
    path('', products_views.all_products, name='all-products-url'),
    path('create/', products_views.create, name='create-products-url'),
    path('details/', products_views.details, name='product-details-url'),
    path('edit/<product_id>', products_views.update, name='update-products-url'),
    path('payment/<product_id>', products_views.payment, name='prodcts-payment-url'),
    path('delete/<product_id>', products_views.delete_product, name='delete-product-url')
]
