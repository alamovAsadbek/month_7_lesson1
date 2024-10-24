from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')
