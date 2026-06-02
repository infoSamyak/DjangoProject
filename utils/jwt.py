import jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, "TEST",
            algorithms=["HS256"],
        )
        return {
            "payload": payload,
            "success": True
        }

    except jwt.ExpiredSignatureError:
        return {
            "success": False,
            "message": "Token is Expired"
        }

    except jwt.InvalidTokenError:
        return {
            "success": False,
            "message": "Token is Invalid"
        }
