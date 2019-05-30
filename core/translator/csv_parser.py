import csv
import os
from register_parsers import RegisterParserFactory


class CsvParser(object):
    class Csv(object):
        def __init__(self, tag, values):
            self.tag = tag
            self.values = values

    def __init__(self):
        self.register_parser = RegisterParserFactory.register_parsers

    def parse(self, xml_path):
        resource = os.path.basename(xml_path)
        root = []
        with open(xml_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            titles = next(csv_reader)
            for row_value in csv_reader:
                row_title_value = dict()
                for i in range(len(titles)):
                    row_title_value[titles[i]] = row_value[i]
                root.append(row_title_value)

        file_info = {
            "path": resource,
            "root": self.Csv(resource, root)
        }
        return self.get_parser(**file_info)

    def get_parser(self, **kwargs):

        for v, register_parser in self.register_parser.items():
            if kwargs.get('root').tag.startswith(register_parser.main_tag):
                return register_parser().parse(kwargs)

        raise NameError('not found')
