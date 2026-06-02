from django.http import JsonResponse, HttpRequest
import json


def users(request: HttpRequest):
    name = ""
    if (request.method == "GET"):
        name = request.GET.get("name", "Guest")
    elif (request.method == "POST"):
        body = json.loads(request.body)
        name = body["name"]
    return JsonResponse({
        "message": f"Hello {name} from POST method"
    })
