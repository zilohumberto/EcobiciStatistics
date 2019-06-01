
from elasticsearch import Elasticsearch

es = Elasticsearch()
# Models allowed
data = {
    'station': [],
    'trip': []
}


def add(key, model):
    data.get(key, []).append(model)

    if key=='station':
        es.index(index="station",
                 doc_type="test-type",
                 body={
                     "name": model.nombre,
                })
        print("everything ok")
        return True
