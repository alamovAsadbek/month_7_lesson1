from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    path('detail/', views.ProductDetailView.as_view(), name='detail'),
]