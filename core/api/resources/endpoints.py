from . import Method
import core.api.controllers as controller


ENDPOINTS = [
    dict(
        controller=controller.StationController,
        endpoint='station',
        methods=[Method.GET, Method.DELETE],
        urls=[
            '/station/'
        ]
    ),
    dict(
        controller=controller.TripController,
        endpoint='trip',
        methods=[Method.GET, Method.DELETE],
        urls=[
            '/trip/'
        ]
    )
]
