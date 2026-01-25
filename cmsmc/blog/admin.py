from django.contrib import admin

from .models import BlogPost
from .models import Series


class BlogPostAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_display = [
        "title",
        "published_at",
        "series",
        "post_type",
    ]
    list_editable = [
        "series",
    ]
    list_filter = [
        "published_at",
        "series",
        "post_type",
    ]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Series)

