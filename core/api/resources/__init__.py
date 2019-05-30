from functools import wraps
from flask import request


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
