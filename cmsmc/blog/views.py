import markdown as md

from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import BlogPost
from .models import Series
from .forms import BlogPostPrimaryForm
from .forms import BlogPostMetaForm

def index_view(request):
    latest = BlogPost.objects.public().first()
    recents = BlogPost.objects.public()[1:6]
    return render(
        request,
        "index.html",
        {"blog_post": latest, "recents": recents},
    )


def blog_post_view(request, year, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if not blog_post.is_published:
        raise Http404()

    return render(
        request,
        "blog/blog_post.html",
        {"blog_post": blog_post},
    )



@login_required
def blog_post_draft_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST" and "publish" in request.POST:
        blog_post.publish()
        return redirect(blog_post.get_absolute_url())

    blog_post.body_html = md.markdown(
        blog_post.body_markdown,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.sane_lists",
            "markdown.extensions.smarty",
            "markdown_sub_sup",
            "markdown_del_ins",
            "markdown_mark",
        ],
    )

    main_form = BlogPostPrimaryForm(instance=blog_post)
    meta_form = BlogPostMetaForm(instance=blog_post)

    return render(
        request,
        "blog/blog_post_draft.html",
        {
            "blog_post": blog_post,
            "blog_post_main_form": main_form,
            "blog_post_meta_form": meta_form
        },
    )


@login_required
def blog_post_edit_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST" and "save" in request.POST:
        main_form = BlogPostPrimaryForm(request.POST, instance=blog_post, label_suffix='')
        meta_form = BlogPostMetaForm(request.POST, instance=blog_post, label_suffix='')
        main_form.save()
        meta_form.save()
    else:
        main_form = BlogPostPrimaryForm(instance=blog_post, label_suffix='')
        meta_form = BlogPostMetaForm(instance=blog_post, label_suffix='')

    return render(
        request,
        "blog/blog_post_edit.html",
        {
            "blog_post": blog_post,
            "blog_post_main_form": main_form,
            "blog_post_meta_form": meta_form
        },
    )



def blog_archive_view(request):
    entries = BlogPost.objects.public()
    return render(request, "blog/blog_archive.html", {"entries": entries})


def blog_series_view(request, slug):
    series = get_object_or_404(Series, slug=slug)
    entries = BlogPost.objects.public().filter(series__slug=slug)
    return render(
        request, "blog/blog_archive.html", {"entries": entries, "series": series}
    )


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
                + """<hr><p><small>Thank you for using RSS</small></p>"""
            )

        return body

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return item.uuid
