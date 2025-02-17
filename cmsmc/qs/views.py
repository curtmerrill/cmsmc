import dotenv
import json
import os

from datetime import datetime, timedelta
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import JournalEntry

dotenv.load_dotenv()

API_KEY = os.environ.get("QS_API_KEY", "Not loaded")


# Create your views here.
@csrf_exempt
def create_entry(request):
    if request.method != "POST":
        return HttpResponse("405 Method Not Allowed", status=405)
    if API_KEY == "Not loaded":
        return HttpResponse("503 Service Unavailable", status=503)
    if (
        "X_QS_API_KEY" not in request.headers
        or request.headers["X_QS_API_KEY"] != API_KEY
    ):
        return HttpResponse("401 Unauthorized", status=401)

    submission = json.loads(request.body)

    if "label" not in submission or (
        "value" not in submission and "body" not in submission
    ):
        return HttpResponse("400 Bad Request", status=400)

    j = JournalEntry.objects.create(label=submission["label"])

    if "value" in submission:
        j.value = submission["value"]

    if "body" in submission:
        j.body = submission["body"]

    j.save()

    return JsonResponse({"status": "201"}, status="201")


@login_required
def label_list(request):
    labels = JournalEntry.objects.order_by().values("label").distinct()

    return render(request, "qs/label_list.html", {"labels": labels})


@login_required
def entry_list(request, label):
    entries = JournalEntry.objects.filter(label=label)

    return render(request, "qs/entry_list.html", {"entries": entries, "label": label})


def framed_summary(request):
    entries = JournalEntry.objects.filter(label="framed")
    framed = [
        {"id": e.value, "seen": e.body["seen"], "guesses": e.body["guesses"]}
        for e in entries
    ]
    last_update = entries[0].created_at.strftime("%c")
    for f in framed:
        if "🟩" in f["guesses"]:
            f["correct_guess"] = 6 - f["guesses"].count("⬛")
        else:
            f["correct_guess"] = -1

    return JsonResponse(
        {"lastUpdate": last_update, "data": framed}, status="201", safe=False
    )


def now_summary(request):
    two_months_ago = datetime.now() - timedelta(days=60)
    recent_entries = JournalEntry.objects.filter(created_at__gt=two_months_ago)

    battery = recent_entries.filter(label="battery").latest("created_at")
    location = recent_entries.filter(label="location").latest("created_at")
    tv = recent_entries.filter(label="tv")
    book = recent_entries.filter(label="book")
    movie = recent_entries.filter(label="movie")

    return JsonResponse(
        {
            "battery": {
                "level": battery.value,
                "timestamp": battery.created_at.isoformat(),
            },
            "location": {
                "place": location.value,
                "timestamp": battery.created_at.isoformat(),
            },
            "tv": list({t.value for t in tv}),
            "movie": list({m.value for m in movie}),
            "book": [
                {"title": b.body["title"], "author": b.body["author"]} for b in book
            ],
        },
        status="201",
        safe=False,
    )
