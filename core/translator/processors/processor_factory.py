from core.translator.processors.processors.station_processor import StationProcessor
from core.translator.processors.processors.trip_processor import TripProcessor


class ProcessorFactory(object):
    _processors = dict(
        STATION_REGISTER=StationProcessor(),
        TRIP_REGISTER=TripProcessor()
    )

    def create(self, register_type):
        return self._processors.get(register_type, None)
