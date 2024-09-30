import json
import os

import dotenv
from django.http import HttpResponse
from django.http import JsonResponse

# from django.shortcuts import render
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
