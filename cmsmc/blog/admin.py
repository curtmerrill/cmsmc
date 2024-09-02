from django.contrib import admin

from .models import BlogPost
from .models import Series


class SeriesAdmin(admin.ModelAdmin):
    pass


class BlogPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Series, SeriesAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
