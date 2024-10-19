from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms import ContactUsModelForm


def home_page_view(request):
    return render(request, 'home.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def login_page_view(request):
    return render(request, 'user-login.html')


def register_page_view(request):
    return render(request, 'user-register.html')


def logout_page_view(request):
    logout(request)
    return redirect('common:home')


class ContactPageView(CreateView):
    template_name = 'contact.html'
    form_class = ContactUsModelForm
    success_url = reverse_lazy("common:home")
