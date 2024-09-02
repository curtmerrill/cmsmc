from django.urls import path

from .views import LatestBlogFeed
from .views import blog_archive
from .views import blog_archive_series
from .views import blog_post
from .views import blog_post_draft_view

# ... LatestBlogFeed, blog_archive_all, blogpost_detail, blogpost_draft

urlpatterns = [
    path("draft/<slug:slug>/", blog_post_draft_view, name="blog_post_draft"),
    path("<int:year>/<slug:slug>/", blog_post, name="blog_post"),
    path("series/<slug:slug>/", blog_archive_series, name="blog_archive_series"),
    path("feed/", LatestBlogFeed()),
    path("", blog_archive, name="blog_archive"),
    # path("feed/", LatestBlogFeed()),
    # path("", blog_archive_all, name="blog_archive"),
]
