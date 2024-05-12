from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    list_display_links = list_display

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
