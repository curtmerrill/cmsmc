from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class JournalEntry(models.Model):
    label = models.CharField(max_length=255)
    value = models.CharField(max_length=255, null=True)
    body = models.JSONField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.label = slugify(self.label)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "journal entries"
