from .controller import Controller
from core.database.model import Trip
from core.api import Entity


class TripController(Controller):
    model = Trip
    entity = Entity.TRIP
