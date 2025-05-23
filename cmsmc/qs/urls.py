from django.urls import path

from .views import create_entry
from .views import entry_list
from .views import framed_summary
from .views import label_list
from .views import now_summary

urlpatterns = [
    path("new", create_entry, name="new_entry"),
    path("browse/<str:label>/", entry_list, name="entry_list"),
    path("browse/", label_list, name="label_list"),
    path("summary/framed/", framed_summary, name="framed_summary"),
    path("summary/now/", now_summary, name="recent_summary"),
]
