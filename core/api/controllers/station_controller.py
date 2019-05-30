from .controller import Controller
from core.database.model import Station
from core.api import Entity


class StationController(Controller):
    model = Station
    entity = Entity.STATION
    model_pk = "nombre"
