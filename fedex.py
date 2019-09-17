import datetime

class Lugar:
    '''Modela los destinos y origen de los envios'''
    def __init__(self, ciudad, pais):
        self.ciudad = ciudad
        self.pais = pais

class Categoria:
    '''Especifica de que rubro es un paquete'''
    def __init__(self, nombre, recargo):
        self.nombre = nombre
        self.recargo = recargo

class Envio:
    '''Paquete enviado por le cliente'''
    def __init__(self, origen, destino, peso, precio_base):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.precio_base = precio_base
        self.categorias = []
        self.fecha = datetime.datetime.now()