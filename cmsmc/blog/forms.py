from django.forms import ModelForm
from django.forms import Textarea
from .models import BlogPost


class BlogPostPrimaryForm(ModelForm):
    template_name = "blog/form_blocks.html"

    class Meta:
        model = BlogPost
        fields = ["title", "subtitle", "body_markdown"]
        widgets = {
            "subtitle": Textarea(attrs={'rows': 2}),
            "body_markdown": Textarea(attrs={'class': 'resize'}),
        }


class BlogPostMetaForm(ModelForm):
    template_name = "blog/form_blocks.html"

    class Meta:
        model = BlogPost
        fields = ["post_type", "series", "slug", "rss_club", "published_at", "og_image"]
