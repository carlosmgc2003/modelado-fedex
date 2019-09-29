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
        self.tiene_recargo = self._activar_recargo()

    def _activar_recargo(self):
        '''Inicializa el booleano tiene_recargo'''
        return self.recargo != 0.0

    def __repr__(self):
        return f'{self.nombre}: {self.recargo * 100}%'


class Envio:
    '''Paquete enviado por le cliente'''

    def __init__(self, origen: Lugar, destino: Lugar, peso, precio_base,categoria):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.precio_base = precio_base
        self.categorias = [].append(categoria)
        self.fecha = datetime.datetime.now()

    def __repr__(self):
        return f'{self.origen}\t{self.destino}\t{self.peso}\t${self.precio_base}\t{self.fecha}'

    def soy_internacional(self):
        return self.origen.pais != self.destino.pais


class Fabrica_envio:
    '''Permite crear un nuevo envío de forma interactiva'''

    def __init__(self, lista_lugares, lista_categorias):
        self.lista_lugares = lista_lugares
        self.lista_categorias = lista_categorias

    def _seleccionar_lugar(self):
        '''Imprime una la lista de lugares del sistema y devuelve el
        seleccionado mediante un indice'''
        print('Seleccione lugar, 0 para crear nuevo')
        for nro, lugar in enumerate(self.lista_lugares):
            print(f'{nro + 1}) {lugar}')
        seleccion = int(input())
        while seleccion not in range(len(self.lista_lugares) + 1):
            print('Entrada no valida, intente nuevamente.')
            seleccion = int(input())
        if seleccion == 0:
            nuevo = self._crear_lugar()
            return nuevo
        else:
            return self.lista_lugares[seleccion]

    def _seleccionar_categoria(self):
        '''Imprime una la lista de lugares del sistema y devuelve el
        seleccionado mediante un indice'''
        print('Seleccione categoria, 0 para crear nueva')
        for nro, lugar in enumerate(self.lista_categorias):
            print(f'{nro + 1}) {lugar}')
        seleccion = int(input())
        while seleccion not in range(len(self.lista_categorias) + 1):
            print('Entrada no valida, intente nuevamente.')
            seleccion = int(input())
        if seleccion == 0:
            nuevo = self._crear_categoria()
            return nuevo
        else:
            return self.lista_categorias[seleccion]

    def _crear_lugar(self):
        pais = input('Ingrese pais:')
        while len(pais) == 0:
            print('Nombre de pais invalido.')
            pais = input('Ingrese pais:')
        ciudad = input('Ingrese ciudad:')
        while len(ciudad) == 0:
            print('Nombre de ciudad invalido.')
            ciudad = input('Ingrese pais:')
        nuevo = Lugar(ciudad=ciudad, pais=pais)
        return nuevo


    def _crear_categoria(self):
        categoria = input('Ingrese categoria:')
        while len(categoria) == 0:
            print('Nombre de categoria invalido.')
            categoria = input('Ingrese categoria:')
        recargo = float(input('Ingrese recargo:'))
        while recargo <= 0:
            print('Recargo de categoria invalido.')
            recargo = float(input('Ingrese recargo:'))
        nuevo = Categoria(nombre=categoria, recargo=(recargo / 100))
        return nuevo

    def _ingresar_peso(self):
        print('Ingrese peso:')
        peso = float(input())
        while peso < 0.0:
            print('Peso incorrecto. Intente nuevamente:')
            peso = float(input())
        return peso

    def _ingresar_precio_base(self):
        print('Ingrese precio base:')
        precio = float(input())
        while precio < 0.0:
            print('Precio base incorrecto. Intente nuevamente:')
            precio = float(input())
        return precio

    def iniciar_fabricacion(self):
        print('Creacion de nuevo envio')
        print('Cree o elija lugar de origen:')
        origen = self._seleccionar_lugar()
        print('Cree o elija lugar de destino')
        destino = self._seleccionar_lugar()
        print('Cree o elija categoria')
        categoria = self._seleccionar_categoria()
        peso = self._ingresar_peso()
        precio = self._ingresar_precio_base()
        return Envio(origen=origen, destino=destino, categoria=categoria, peso=peso, precio_base=precio)
