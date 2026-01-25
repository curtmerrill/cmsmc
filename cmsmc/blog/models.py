import uuid
import markdown as md
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

POST_TYPES = [
    ("a", "article"),
    ("p", "photo"),
    ("t", "tweet"),
]

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
        return(
            super()
            .get_queryset()
            .filter(
                published_at__isnull=False,
                published_at__lte=timezone.now()
            )
            .order_by("-published_at")
        )


class Series(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Series: {self.name}"

    def get_absolute_url(self):
        return reverse("blog_series_view", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]
        verbose_name_plural = "series"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)
    subtitle = models.TextField(blank=True, null=True)

    post_type = models.CharField(
        max_length=1,
        choices=POST_TYPES,
        default="a",
    )
    rss_club = models.BooleanField(default=False)
    series = models.ForeignKey(Series, models.SET_NULL, blank=True, null=True)

    primary_image = models.ImageField(
        blank=True,
        null=True,
        max_length=511,
        upload_to="media/%Y/"
    )
    og_image = models.CharField(max_length=511, blank=True, null=True)

    body_markdown = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True, editable=False)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )


    objects = BlogPostManager()

    def __str__(self):
        return f"{self.post_type}: {self.title} ({self.created_at.year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.primary_image and not self.og_image:
            self.og_image = self.primary_image.url
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

    def get_absolute_url(self):
        return reverse("blog_post_view", kwargs={"year": self.created_at.year, "slug": self.slug})

    class Meta:
        ordering = ["-created_at",]

