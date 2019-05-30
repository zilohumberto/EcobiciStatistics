from flask_restful import Resource
from flask import request


class BaseResource(Resource):
    controller = None

    def __init__(self):
        self._controller = self.controller()

    def delete(self, **kwargs):
        return self._controller.delete(**kwargs), 204

    def get(self, **kwargs):
        if kwargs.get('id') is not None:
            return self._controller.get(**kwargs), 200
        return self._controller.get_collection(args=request.args.to_dict(), **kwargs), 200
