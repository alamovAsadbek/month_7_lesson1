from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, CategoryModel, TagModel, BrandModel, ColorModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'products/product-list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        return context


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'products/product-detail.html'
    context_object_name = 'products'
