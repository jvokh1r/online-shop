from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
