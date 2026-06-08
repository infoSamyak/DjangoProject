from django.http import JsonResponse, HttpRequest
import json
import jwt
from datetime import datetime, timedelta, timezone


def login(request: HttpRequest):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        print(body)
        token = jwt.encode({
            "id": body["id"],
            "name": body["name"],
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=60)
        }, "TEST", algorithm="HS256",)
        print(body)
        return JsonResponse({
            "token": token,
        })
