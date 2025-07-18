import markdown as md
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)

    body_markdown = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True, editable=False)

    updated_at = models.DateTimeField(auto_now=True)

    def publish(self, *args, **kwargs):
        self.body_html = md.markdown(
            self.body_markdown,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.sane_lists",
                "markdown.extensions.smarty",
                "markdown_sub_sup",
                "markdown_del_ins",
                "markdown_mark",
            ],
        )

        self.save(*args, **kwargs)

    def __str__(self):
        return f"Page {self.title}"

    class Meta:
        ordering = ["title"]
