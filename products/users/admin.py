from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'is_active', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('created_at', 'is_active')
