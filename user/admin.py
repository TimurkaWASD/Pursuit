from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'photo', 'description', 'languages', 'country')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'photo', 'description', 'languages', 'country')}),
    )
    list_display = ('username', 'email', 'first_name', 'second_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'second_name')
    ordering = ('username',)
    readonly_fields = ['date_joined']

admin.site.register(CustomUser, CustomUserAdmin)