import markdown as md
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import BlogPost


def blog_post(request, year, slug):
    entry = get_object_or_404(BlogPost, slug=slug)
    return render(
        request,
        "blog/blog_post.html",
        {"blog_post": entry},
    )


# Create your views here.
@login_required
def blog_post_draft_view(request, slug):
    entry = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST" and "publish" in request.POST:
        entry.publish()

        return redirect(entry.get_absolute_url())

    post_body = md.markdown(
        entry.body_markdown,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.sane_lists",
            "markdown.extensions.smarty",
            "markdown_sub_sup",
            "markdown_del_ins",
            "markdown_mark",
        ],
    )

    return render(
        request,
        "blog/blog_post.html",
        {
            "blog_post": entry,
            "post_body": post_body,
            "draft": True,
        },
    )


def blog_archive(request):
    entries = BlogPost.objects.public()
    return render(request, "blog/blog_archive.html", {"entries": entries})


def blog_archive_series(request, slug):
    entries = BlogPost.objects.public().filter(series__slug=slug)
    return render(request, "blog/blog_archive_series.html", {"entries": entries})


class LatestBlogFeed(Feed):
    title = "curtmerrill.com"
    link = "/"
    description = "Latest blog entries"

    def items(self):
        entries = BlogPost.objects.rss_club()[:10]
        return entries

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        body = item.body_html

        if item.rss_club:
            body = (
                """<p><small>
                  It’s a secret to everyone! <a href="https://daverupert.com/2018/01/welcome-to-rss-club/">Read more about RSS Club</a>.
                </p></small></p>"""
                + item.body_html
            )

        return body

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return item.uuid
