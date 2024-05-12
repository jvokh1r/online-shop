from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = list_display
    readonly_fields = ('last_login',)
    fields = ('email', 'first_name', 'last_name', 'phone_number', 'password')

    def save_model(self, request, obj, form, change):
        if obj.password != form.initial.get("password"):
            obj.set_password(obj.password)
        obj.save()


admin.site.register(CustomUser, CustomUserAdmin)
