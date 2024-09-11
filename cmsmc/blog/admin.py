from django.contrib import admin

from .models import BlogPost
from .models import Series


class SeriesAdmin(admin.ModelAdmin):
    pass


class BlogPostAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_display = [
        "title",
        "published_at",
        "series",
    ]
    list_editable = [
        "series",
    ]
    list_filter = [
        "published_at",
        "series",
    ]


admin.site.register(Series, SeriesAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
