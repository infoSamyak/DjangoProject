from django.http import JsonResponse, HttpRequest
from .models import Users


def get_users(request: HttpRequest):
    if (request.method != "GET"):
        return JsonResponse({
            "error": "Method Not Allowed",
        }, status=405)

    try:
        users = Users.objects.all()
        data = [
            {
                "id": u.id,
                "first_name": u.fname,
                "last_name": u.lname,
                "age": u.age
            }
            for u in users
        ]

        return JsonResponse({
            "message": "Users fetched successfully",
            "data": data
        })
    except:
        return JsonResponse({
            "error": "usersØ not found"
        }, status=404)


def get_user(request: HttpRequest, id: int):
    if (request.method != "GET"):
        return JsonResponse({
            "error": "Method Not Allowed",
        }, status=405)

    try:
        user = Users.objects.get(id=id)
        data = {
            "id": user.id,
            "first_name": user.fname,
            "last_name": user.lname,
            "age": user.age
        }
        return JsonResponse({
            "message": "Users fetched successfully",
            "data": data
        })
    except:
        return JsonResponse({
            "error": "user not found"
        }, status=404)
