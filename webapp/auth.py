import re
from bumbo.middleware import Middleware

STATIC_TOKEN = "ae4CMvqBe2"


class InvalidTokenException(Exception):
    pass


def login_required(handler):
    def wrapped_view(request, response, *args, **kwargs):
        token = getattr(request, "token", None)

        if token is None or not token == STATIC_TOKEN:
            raise InvalidTokenException("Invalid Token")

        return handler(request, response, *args, **kwargs)

    return wrapped_view
