from django.contrib import admin

from .models import Post, Author, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # fields = ("title", "author", "excerpt", "content", "slug", "image_name", "date", "tags")
    # exclude = ("date",)
    list_display = ("title", "date", "author")
    list_filter = ("author", "tags", "date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
