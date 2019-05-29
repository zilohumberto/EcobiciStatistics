from core.translator.parsers.stations_parser import StationsParser
from core.translator.parsers.trip_parser import TripParser


class RegisterParserFactory(object):
    register_parsers = dict(
        STATION_REGISTER=StationsParser,
        TRIP_REGISTER=TripParser
    )
