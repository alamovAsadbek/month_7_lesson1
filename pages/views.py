from django.shortcuts import render

from pages.models import BlogModel


def home_page_view(request):
    return render(request, 'home.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def about_page_view(request):
    return render(request, 'about-us.html')


def blog_page_view(request):
    blogs = BlogModel.objects.all().order_by('-created_at')[:6]
    recent_blogs = BlogModel.objects.all().order_by('-updated_at')[:3]
    context = {
        "blogs": blogs,
        "recent_blogs": recent_blogs,
    }
    return render(request, 'blog-list.html', context)
