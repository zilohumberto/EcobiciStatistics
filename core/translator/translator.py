import os
from core.translator.processors.processor_factory import ProcessorFactory
from csv_parser import CsvParser


class Translator(object):

    def __init__(self):
        self._parser = {
            '.csv': CsvParser()
        }
        self.processor_factory = ProcessorFactory()

    def translate(self, file_path):
        try:
            parsed = self._get_parser(file_path).parse(file_path)
            for register in parsed:
                try:
                    processor = self.processor_factory.create(
                       register.get('register_type'))
                    processor.process(register)

                except Exception as e:
                    pass

        except Exception as e:
            raise NameError(e.message)

    def _get_parser(self, file_path):
        filename, file_extension = os.path.splitext(file_path)
        return self._parser.get(file_extension, ".csv")
