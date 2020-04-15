from django.contrib import admin
from .models import Post, Tag, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
