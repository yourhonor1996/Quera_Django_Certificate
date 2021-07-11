from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'national_code',
                'father_name',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username',
        'email',
        'father_name',
    )

    search_fields = (
        'username',
        'email',
    )