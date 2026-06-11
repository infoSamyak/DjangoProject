from typing import Any

from rest_framework.response import Response


class SuccessResponse(Response):
    def __init__(self, data: Any = None, status=200, **kwargs):
        super().__init__(
            {"success": True,   "data": data, },
            status=status,
            **kwargs
        )


class ErrorResponse(Response):
    def __init__(self, message="Something went wrong", status=500, **kwargs):
        super().__init__(
            {"success": False, "message": message},
            status,
            **kwargs
        )
