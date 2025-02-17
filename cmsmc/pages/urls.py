from django.urls import path

from .views import page_view
from .views import page_draft_view
from .views import site_index

urlpatterns = [
    path("", site_index, name="index"),
    path("<slug:slug>/draft/", page_draft_view, name="page_draft"),
    path("<slug:slug>/", page_view, name="page_view"),
]
