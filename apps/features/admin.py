from django.contrib import admin
from .models import Feature, FeatureValue, ProductFeature


class FeatureValueInline(admin.StackedInline):
    model = FeatureValue
    prepopulated_fields = ({"slug": ('value',)})


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('name',)}
    inlines = [FeatureValueInline]


@admin.register(FeatureValue)
class FeatureValue(admin.ModelAdmin):
    list_display = ('feature', 'value', 'price')
    list_display_links = list_display
    list_filter = ['feature']
    prepopulated_fields = {"slug": ('value',)}


@admin.register(ProductFeature)
class ProductFeature(admin.ModelAdmin):
    list_display = ('product', 'feature_value')
    list_display_links = list_display
    list_filter = ['product']
