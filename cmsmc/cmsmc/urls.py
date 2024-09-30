from blog.views import site_index
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", site_index, name="index"),
    path("blog/", include("blog.urls")),
    path("qs/", include("qs.urls")),
    path("now/", views.flatpage, {"url": "/now/"}, name="now"),
    path("uses/", views.flatpage, {"url": "/uses/"}, name="uses"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()
