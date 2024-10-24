from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext_lazy as _

from pages.admin import ContactModel
from pages.forms import ContactModelForm


class ContentView(TemplateView):
    template_name = 'pages/contact.html'


class HomeView(TemplateView):
    template_name = 'pages/home.html'


# blogs
class BlogListView(TemplateView):
    template_name = 'blogs/blog-list.html'


class BlogDetailView(TemplateView):
    template_name = 'blogs/blog-detail.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'


class CartView(TemplateView):
    template_name = 'ordering/cart.html'


class WishlistView(TemplateView):
    template_name = 'ordering/user-wishlist.html'


class CheckoutView(TemplateView):
    template_name = 'ordering/checkout.html'


class ContactCreateView(CreateView):
    model = ContactModel
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('pages:create')
    success_message = _('Your message is submitted!')
