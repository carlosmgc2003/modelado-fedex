import datetime

class Lugar:
    '''Modela los destinos y origen de los envios'''
    def __init__(self, ciudad, pais):
        self.ciudad = ciudad
        self.pais = pais

    def __repre__(self):
        return f'{self.ciudad}, {self.pais}'

    def __str__(self):
        return f'{self.ciudad}, {self.pais}'

class Categoria:
    '''Especifica de que rubro es un paquete'''
    def __init__(self, nombre, recargo):
        self.nombre = nombre
        self.recargo = recargo
        self.tiene_recargo = self.activar_recargo()

    def activar_recargo(self):
        '''Inicializa el booleano tiene_recargo'''
        return self.recargo != 0.0

    def __repr__(self):
        return f'{self.nombre}: {self.recargo * 100}%'

class Envio:
    '''Paquete enviado por le cliente'''
    def __init__(self, origen, destino, peso, precio_base):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.precio_base = precio_base
        self.categorias = []
        self.fecha = datetime.datetime.now()

    def __repr__(self):
        return f'{self.origen}\t{self.destino}\t{self.peso}\t${self.precio_base}\t{self.fecha}'