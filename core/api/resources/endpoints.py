from . import Method
import core.api.controllers as controller


ENDPOINTS = [
    dict(
        controller=controller.Controller,
        endpoint='station',
        methods=[Method.GET, Method.DELETE],
        urls=[
            '/station/'
        ]
    )
]
