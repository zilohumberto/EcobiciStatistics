from functools import wraps
from flask import request
from core.api.exceptions import BadRequestException
from core.api.resources.authentication import Authenticator
from core.api.messages import CONTENT_TYPE_SUPPORTED


class Method(object):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class Status(object):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_ERROR = 500


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        Authenticator.authenticate(request.headers.get('Authorization', ''))
        return f(*args, **kwargs)
    return decorated


def content_type(accepted):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            headers = {header.lower(): value for header, value in request.headers.items()}
            _content_type = 'content-type'
            if _content_type not in headers or headers.get(_content_type).lower() != accepted:
                raise BadRequestException(CONTENT_TYPE_SUPPORTED.format(accepted, _content_type))
            return func(*args, **kwargs)
        return wrapper
    return real_decorator


def add_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        json_response, status_code = f(*args, **kwargs)
        return json_response, status_code, dict(Authorization=Authenticator.token)
    return decorated


def add_endpoints(api):
    from core.api.resources.resource import BaseResource
    from core.api.resources.endpoints import ENDPOINTS

    for endpoint in ENDPOINTS:
        class CustomResource(BaseResource):
            controller = endpoint['controller']

        api.add_resource(
            CustomResource,
            *endpoint['urls'],
            endpoint=endpoint['endpoint'],
            methods=endpoint['methods']
        )
