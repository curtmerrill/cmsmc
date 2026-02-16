from django.urls import path

from .views import blog_post_view
from .views import blog_post_draft_view
from .views import blog_post_edit_view
from .views import blog_archive_view
from .views import blog_series_view
from .views import LatestBlogFeed

urlpatterns = [
    path("<int:year>/<slug:slug>/", blog_post_view, name="blog_post_view"),
    path("series/<slug:slug>/", blog_series_view, name="blog_series_view"),
    path("draft/<slug:slug>/", blog_post_draft_view, name="blog_post_draft_view"),
    path("edit/<slug:slug>/", blog_post_edit_view, name="blog_post_edit_view"),
    path("feed/", LatestBlogFeed(), name="latest_entries_rss"),
    path("", blog_archive_view, name="blog_archive_view"),
]
