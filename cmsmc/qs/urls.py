from django.urls import path

from .views import create_entry

urlpatterns = [
    path("new", create_entry, name="new_entry"),
]
