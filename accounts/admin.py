from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

    fieldsets = ()
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal Info', {'fields': ('first_name', 'last_name', 'username', 'phone')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser')}),
    #     ('Important dates', {'fields': ()}),  # Exclude 'date_joined' and 'last_login'
    # )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'phone'),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()

admin.site.register(Account, AccountAdmin)
