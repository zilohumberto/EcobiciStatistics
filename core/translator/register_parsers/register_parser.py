from lxml import etree


class RegisterParser(object):
    main_tag = None
    schema = None

    def parse(self, register):
        try:
            self._validate(register)
            self._debug_parser(register)
            return self._get_parsed_register(register)

        except NotImplementedError as e:
            raise NotImplemented(e)
        except etree.DocumentInvalid as e:
            raise etree.DocumentInvalid(e)

    def _get_parsed_register(self, register):
        raise NotImplementedError()

    def _validate(self, register):
        raise NotImplementedError()

    def _debug_parser(self, register):
        raise NotImplementedError()
