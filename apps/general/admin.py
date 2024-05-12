from django.contrib import admin
from . import models as general_models


@admin.register(general_models.General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_name',)
    list_display_links = list_display

    def has_add_permission(self, request):
        return not general_models.General.objects.exists()


@admin.register(general_models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('title',)}


@admin.register(general_models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('title',)}


@admin.register(general_models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('title',)}


@admin.register(general_models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


@admin.register(general_models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('name',)}


@admin.register(general_models.PaymentMethod)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('name',)}
