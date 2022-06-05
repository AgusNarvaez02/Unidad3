from ObjectEncoder import ObjectEncoder
from Heladeras import Heladeras
from Lavarropas import Lavarropas
from Televisores import Televisores
from ManejadorInterface import ManejadorInterface
from ClaseLista import Lista

class Menu:
    __clasLista: Lista
    def __init__(self):
        self.__clasLista= Lista()
    
    def opciones(self):
        print('1. Crear archivo JSON \n')
        print('2. Insertar un aparato en la colección en una posición determinada \n')
        print('3. Agregar un aparato a la colección \n')
        print('4. Dada una posición de la Lista: Mostrar qué tipo de objeto se encuentra almacenado en dicha posición \n')
        print('5. Mostrar  la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips\n ')
        print('6. Mostrar la marca de todos los lavarropas que tienen carga superior\n ')
        print('7. Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta \n')
        print('8. Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json” \n')
    
    def cargararchJSON(self, json):
        ob1= Heladeras('Patrick', 'HPK135MOOB01', 'Blanca', 'Argentina', 60000, 2770, True, True)
        ob2= Lavarropas('Samsung', 'WW65MONHWU', 'Negro', 'Argentina', 70000, 6, 1000, 2, 'Superior')
        ob3= Televisores('Phillips', '43PFD6825', 'Negro', 'Argentina', 45000, 'LCD', 43, 'HD', True )

        d1= ob1.toJson()
        d2= ob2.toJson()
        d3= ob3.toJson()
        lista= [d1, d2, d3]
        json.guardarJSONarchivo(lista, 'Aparatos.json')

    def Menuop(self):
        manInterfaz= ManejadorInterface()
        Json= ObjectEncoder()
        Json.decodificadorDiccionario(self.__clasLista)
        self.opciones()
        op= int(input('Ingrese una opcion distinta de 0'))
        while o!= 0:
            if op==1:
                self.cargararchJSON(Json)
            elif op==2:
                manInterfaz.llamaInterface(self.__clasLista, op)
            elif op== 3:
                manInterfaz.llamaInterface(self.__clasLista, op)
            elif op== 4:
                manInterfaz.llamaInterface(self.__clasLista, op)
            elif op==5:
                c= self.__clasLista.ctPhil()
                if c!=0:
                    print('Cantidad de aparatos Phillips= {}' .format(c))
                else:
                    print('No hay aparatos Phillips')
            
            elif op== 6:
                self.__clasLista.superior()
            
            elif op== 7:
                self.__clasLista.MostrarAparatos()
            
            elif op== 8:
                self.__clasLista.almacenar(Json)
            self.opciones()
            op= int(input('Ingrese una opcion distinta de 0'))



