

class Transaction(object):
    id = None


class Parametric(object):
    code = None


class Station(Parametric):
    long = None
    lat = None
    nombre = None
    domicilio = None
    image = None
    automat = None
    observ = None
    resource = None


class Trip(Parametric):
    bici_id_usuario = None
    bici_Fecha_hora_retiro = None
    bici_tiempo_uso = None
    bici_nombre_estacion_origen = None
    bici_estacion_origen = None
    bici_nombre_estacion_destino = None
    bici_estacion_destino = None
    bici_sexo = None
    bici_edad = None
