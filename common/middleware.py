from django.http import JsonResponse, HttpRequest, HttpResponse
from utils import jwt


class ClientMiddleware:
    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        client_id = request.headers.get("client-id")
        client_secret = request.headers.get("client-secret")
        auth_token = request.headers.get("Authorization")

        if not client_id:
            return JsonResponse({
                "status": "failed",
                "message": "client-id is missing"
            }, status=400)
        elif not client_secret:
            return JsonResponse({
                "status": "failed",
                "message": "client-secret is missing"
            }, status=400)
        elif (client_id != "Text"):
            return JsonResponse({
                "status": "failed",
                "message": "Invalid client-id"
            }, status=401)
        elif (client_secret != "Test"):
            return JsonResponse({
                "status": "failed",
                "message": "Invalid client-id"
            }, status=401)

        if (request.path.startswith("/api/")):

            if not auth_token:
                return JsonResponse({
                    "status": "failed",
                    "message": "Authorization is missing"
                }, status=400)

            verified_token = jwt.verify_token(auth_token)
            if (verified_token["success"] == False):
                return JsonResponse({
                    "status": "failed",
                    "message": verified_token["message"]
                }, status=401)

        request.client_id = client_id

        request.client_secret = client_secret

        response = self.get_response(request)

        return response
