from core.translator.processors.processor import Processor
from core.database.model import (Trip)
from core.database.data import add


class TripProcessor(Processor):

    def _do_process(self, register):
        trip = register.get('trip')
        resource = register.get('resource')
        instance = Trip
        self._update_instance_with_dict(
            instance, trip)
        instance.resource = resource
        add('trip', instance)
