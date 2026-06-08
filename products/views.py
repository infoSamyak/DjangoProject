from django.http import JsonResponse, HttpRequest
from .models import Product


def products(request: HttpRequest):
    """GET /api/products - return a JSON list of products."""
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    qs = Product.objects.all().order_by("-created_at")
    data = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": str(p.price),
            "created_at": p.created_at.isoformat(),
        }
        for p in qs
    ]

    return JsonResponse({"products": data})
