import os
from core.translator.parsers.fields import TripFields as Fields
from core.translator.register_parsers.register_parser_csv import RegisterCsvParser


class TripParser(RegisterCsvParser):
    main_tag = Fields.MAIN_TAG

    @classmethod
    def _get_parsed_register(cls, register):
        resource = os.path.basename(register['path'])
        _list = register['root'].values
        cls._validated_columns(_list)
        return [
            dict(
                register_type='TRIP_REGISTER',
                resource=resource,
                trip=trip
            )
            for trip in _list
        ]

    @staticmethod
    def _validated_columns(_list):
        pass
