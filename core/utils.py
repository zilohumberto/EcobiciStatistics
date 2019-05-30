from datetime import datetime
from core.settings import API_DATE_FORMAT


def convert_to(value, attr_type):
    types_map = dict(
        INTEGER=int,
        FLOAT=float,
        DATE=convert_to_date
    )
    return types_map.get(attr_type.upper(), str)(value)


def convert_to_date(date_string):
    return datetime.strptime(date_string, API_DATE_FORMAT)


def convert_to_string(date):
    return date.strftime(API_DATE_FORMAT)
