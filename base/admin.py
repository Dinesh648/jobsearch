from django.contrib import admin
from .models import Room, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('organisation', 'workEmail')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room)