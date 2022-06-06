from ManejadorCalefactores import ManejadorCalefactores
class Menu:
    __manCalef: ManejadorCalefactores

    def __init__(self):
        self.__manCalef= ManejadorCalefactores()
        self.__manCalef.cargarCgas()
        self.__manCalef.cargarCelectrico()
    
    def Menu_op(self):
        print('1- Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2 - Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3 - Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo')
        op=int(input('Ingrese una opcion, 0 para finalizar: '))
        while op!=0:
            if op==1:
                c=input('Ingrese el costo por metro al cubo: ')
                h= input('Ingrese cantidad que se estima consumir por hora: ')
                self.__manCalef.mingas(c, h)
            if op==2:
                c=input('Ingrese el costo por metro al cubo: ')
                h= input('Ingrese cantidad que se estima consumir por hora: ')
                self.__manCalef.minelectrico(c, h)
            elif op == 3:
                c=input('Ingrese el costo por metro al cubo: ')
                h= input('Ingrese cantidad que se estima consumir por hora: ')
                self.__manCalef.item_3(c,h)
            
            print('1- Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2 - Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3 - Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo')
            op=int(input('Ingrese una opcion, 0 para finalizar: '))
            