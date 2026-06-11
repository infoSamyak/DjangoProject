from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from products.serializers import ProductSerializer
from utils.responses import ErrorResponse, SuccessResponse
from .models import Product


@api_view(["GET", "POST", "PUT"])
def products(request: Request, id: int | None = None):
    try:
        if request.method == 'GET':
            if id:
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product)
                return SuccessResponse(serializer.data)

            else:
                products = Product.objects.all().order_by("-created_at")
                serializer = ProductSerializer(products, many=True)
                return SuccessResponse(serializer.data)

        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(serializer.data)

            else:
                return ErrorResponse(
                    "Please check request body",
                    status.HTTP_400_BAD_REQUEST
                )

        elif request.method == 'PUT':
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(serializer.data)

            else:
                return ErrorResponse(
                    "Please check request body",
                    status.HTTP_400_BAD_REQUEST
                )

        else:
            return ErrorResponse("Method type is invalid", status.HTTP_404_NOT_FOUND)

    except Product.DoesNotExist:
        return ErrorResponse("Product not found", status.HTTP_404_NOT_FOUND)
