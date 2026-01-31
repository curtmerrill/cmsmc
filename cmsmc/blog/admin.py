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
        "is_published",
    ]
    list_editable = [
        "series",
        "is_published",
    ]
    list_filter = [
        "published_at",
        "series",
        "post_type",
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Series)
