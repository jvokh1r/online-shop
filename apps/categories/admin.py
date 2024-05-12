from django.contrib import admin
from .models import Category, SubCategory


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    prepopulated_fields = {"slug": ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
    prepopulated_fields = {"slug": ('name',)}
    inlines = [SubCategoryInline]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name')
    list_display_links = list_display
    list_filter = ['category']
    search_fields = ['name',]
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
