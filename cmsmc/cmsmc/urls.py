from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include
from django.urls import path
from pages.views import site_index

urlpatterns = [
    path("blog/", include("blog.urls")),
    path("qs/", include("qs.urls")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("pages.urls")),
] + debug_toolbar_urls()
