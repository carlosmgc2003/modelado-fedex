import fedex
class App:
    def __init__(self):
        self.envios = []
        self.lugares_existentes = []
        self.categorias_existentes = []

    def mostar_menu(self):
        '''Metodo dummi que solo imprime menu TODO: Implementarlo de forma mas pitónica'''
        print('Bienvenido al sistema de FedeX')
        print('Por favor, elija la opcion\n')
        print('1) Cargar un nuevo envio')
        print('2) Listar todos los envios')
        print('3) Borrar un envío')
        print('4) Listar todos los envios internacionales')
        print('5) Conocer el precio de un envío')
        print('6) Conocer el envio "propicio a perderse"')
        print('\nIngrese la opcion deseada (0 para salir):')

    def interactividad(self):
        self.mostar_menu()
        self.opcion_seleccionada = input()
        while self.opcion_seleccionada in range(7):
            if self.opcion_seleccionada == 1:
                self.envios.append(fedex.Fabrica_envio(self.lugares_existentes, self.categorias_existentes))
            elif self.opcion_seleccionada == 2: self.listar_envios()
            elif self.opcion_seleccionada == 3: self.borrar_envios()
            elif self.opcion_seleccionada == 4: self.listar_envios_internacionales()
            elif self.opcion_seleccionada == 5: self.conocer_precio_envio()
            elif self.opcion_seleccionada == 6: self.conocer_propicio_a_perderse()
            elif self.opcion_seleccionada == 0: break
            else: print('Error, opcion incorrecta intente nuevamente [0-6]')




    def listar_envios(self):
        '''Imprime en pantalla todos los envios creados en el sistema'''
        for nro, env in enumerate(envios):
            print(f'{nro}) {env}')

    def borrar_envios(self):
        '''Borra un envio mediante un indice'''
        print("Elija el numero de envío a borrar:")
        self.listar_envios()
        nro_a_borrar = input()
        if nro_a_borrar in len(self.envios):
            self.envios.remove(self.envios[nro_a_borrar])

    def listar_envios_internacionales(self):
        '''Imprime en pantalla todos aquellos envios cuyo pais de origen sea diferente al de destino'''
        for nro, env in enumerate(list(filter(lambda env: env.soy_internacional(), self.envios))):
            print(f'{nro}) {env}')

    def conocer_precio_envio(self):
    '''TODO: Implementar impuestos'''
        pass

    def conocer_propicio_a_perderse(self):
    '''TODO: Implementar propicio a perderse'''
        pass


