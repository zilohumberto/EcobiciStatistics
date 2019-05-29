from register_parser import RegisterParser


class RegisterCsvParser(RegisterParser):
    main_tag = None
    schema = None

    def _validate(self, register):
        """ Validate the csv register """
        # La validacion se hizo en los parse de cada producto debido a que no habia manera
        # de validar las columnas de manera unica
        pass

    def _debug_parser(self, register):
        pass

    def _get_parsed_register(self, register):
        raise NotImplementedError()
