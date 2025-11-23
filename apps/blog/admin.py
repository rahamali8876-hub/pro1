from django.contrib import admin

# Register your models here.
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at", "updated_at", "author")


admin.site.register(BlogPost, BlogPostAdmin)
