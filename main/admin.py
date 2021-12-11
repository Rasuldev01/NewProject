from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'is_staff',
        'is_active',
        'image'
    )
    class Meta:
        model = User


admin.site.register(User, UserAdmin)