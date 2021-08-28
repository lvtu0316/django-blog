from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_at', 'status']
    fields = ['name', 'email', 'url', 'text', 'post', 'status']
    '''自定义actions'''
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status=1)

    make_published.short_description = "审核通过"


admin.site.register(Comment, CommentAdmin)

