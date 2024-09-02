import uuid

import markdown as md
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class BlogPostManager(models.Manager):
    def public(self):
        return (
            super()
            .get_queryset()
            .filter(
                rss_club=False,
                published_at__isnull=False,
                published_at__lte=timezone.now(),
            )
            .order_by("-published_at")
        )

    def rss_club(self):
        return (
            super()
            .get_queryset()
            .filter(published_at__isnull=False, published_at__lte=timezone.now())
            .order_by("-published_at")
        )


class Series(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Series: {self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "series"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)

    body_markdown = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True, editable=False)

    rss_club = models.BooleanField(default=False)

    series = models.ForeignKey(
        "Series",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    objects = BlogPostManager()

    def get_absolute_url(self):
        if self.published_at:
            y = self.published_at.year
            return reverse("blog_post", kwargs={"year": y, "slug": self.slug})
        else:
            return reverse("blog_post_draft", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug == slugify(self.title)
        super().save(*args, **kwargs)

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

        if not self.published_at:
            self.published_at = timezone.now()

        self.save(*args, **kwargs)

    def __str__(self):
        if self.published_at:
            return f"{self.title} ({self.published_at.year})"
        else:
            return f"{self.title} (draft)"

    class Meta:
        ordering = ["-published_at"]
