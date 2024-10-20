from django.urls import path

from products.views import products_page_view

app_name = "products"

urlpatterns = [
    path("", products_page_view, name="list"),
]