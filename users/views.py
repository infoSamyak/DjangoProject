from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.responses import ErrorResponse, SuccessResponse

from .models import Users
from .serializers import UserSerializer


@api_view(["GET"])
def get_users(_):
    try:
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)

        return SuccessResponse(serializer.data)

    except:
        return ErrorResponse(
            "users not found",
            status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def get_user(_, id: int):
    try:
        user = Users.objects.get(id=id)
        serialize = UserSerializer(user)

        return SuccessResponse(serialize.data)

    except:
        return ErrorResponse(
            "User not found",
            status.HTTP_404_NOT_FOUND
        )
