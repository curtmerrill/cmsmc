import markdown as md
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Page


def site_index(request):
    first_entry = BlogPost.objects.public().first()
    entries = BlogPost.objects.public()[1:6]
    return render(request, "index.html", {"blog_post": first_entry, "entries": entries})


def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(
        request,
        "pages/page.html",
        {"page": page},
    )


@login_required
def page_draft_view(request, slug):
    page = get_object_or_404(Page, slug=slug)

    if request.method == "POST" and "publish" in request.POST:
        page.publish()

        return redirect(page.get_absolute_url())

    page_body = md.markdown(
        page.body_markdown,
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
        "pages/page.html",
        {
            "page": page,
            "page_body": page_body,
            "draft": True,
        },
    )
