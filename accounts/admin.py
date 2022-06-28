from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User


class LoginUserAdmin(UserAdmin):
    model = User
    list_display = ["username", "email", "auth_provider", "first_name", "last_name"]
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "is_company",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "card_id_img",
                    "last_login",
                )
            },
        ),
        ('Permistions', {
                "fields": (
                    'is_staff','is_active','is_superuser','groups'
                )
            },),
    )


admin.site.register(User, LoginUserAdmin)
