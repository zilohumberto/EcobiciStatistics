
# Models allowed
data = {
    'station': [],
    'trip': []
}


def add(key, model):
    data.get(key, []).append(model)
