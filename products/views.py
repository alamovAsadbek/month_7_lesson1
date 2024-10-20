from django.shortcuts import render
from products.models import *

def products_page_view(request):
    products = ProductModel.objects.all().order_by('-pk')
    categories = CategoryModel.objects.all().order_by('-pk')
    companies = CompanyModel.objects.all().order_by('-pk')
    colors = ColorModel.objects.all().order_by('-pk')
    tags = TagModel.objects.all().order_by('-pk')
    context = {
        "products": products,
        "categories": categories,
        "colors": colors,
        "tags": tags,
        "companies": companies
    }
    return render(request, 'product-list.html', context)