import jwt
from django.conf import settings
import graphql_jwt
from datetime import timedelta


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if "token" not in request.COOKIES:
            if "refresh_token" in request.COOKIES:
                refresh_token = request.COOKIES["refresh"]

                # Use the refresh token to obtain a new JWT and revoke the previous refresh token
                new_token, new_refresh_token = graphql_jwt.refresh_token(
                    refresh_token, revoke=True
                )
                # response.set_cookie("token", new_token, max_age=3600)
                # response.set_cookie("refresh", new_refresh_token, max_age=3600)

                request.COOKIES["token"] = new_token
                request.COOKIES["refresh"] = new_refresh_token

        response = self.get_response(request)
        return response
