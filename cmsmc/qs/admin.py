from django.contrib import admin

from .models import JournalEntry


class JournalEntryAdmin(admin.ModelAdmin):
    list_display = [
        "label",
        "value",
        "created_at",
    ]


admin.site.register(JournalEntry, JournalEntryAdmin)
