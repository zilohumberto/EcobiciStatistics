from core.translator.processors.processor import Processor
from core.database.model import (Station)
from core.database.data import add


class StationProcessor(Processor):

    def _do_process(self, register):
        station = register.get('station')
        resource = register.get('resource')
        instance = Station
        self._update_instance_with_dict(
            instance, station)
        instance.resource = resource
        add('station', instance)
