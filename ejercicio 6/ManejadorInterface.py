from Interfaz import Interfaz
from ClaseLista import Lista
from ObjectEncoder import ObjectEncoder
class ManejadorInterface:
    __controladorO= ObjectEncoder

    def opc(self, lista: Interfaz, op):
        if op== 2:
            ob= self.__controladorO.retornarObj()
            p= int(input('Ingrese posicion donde se incertarael objeto: '))
            if ob != None:
                lista.insertarElemento(p, ob)
            else: 
                print('Objeto incorrecto \n')
        
        elif op== 3:
            ob= self.__controladorO.retornarObj()
            if ob!= None:
                lista.insertarFinal(ob)
            else: print('ERROR\n')
        elif op== 4:
            p= int(input('Ingrese alguna posicion de la lista \n'))
            date= lista.tipoObj(p)
            if date != None:
                print('Tipo de dato: {}'.format(date.getTipo))
            
            else: print('Pocision eeronea \n')
        
    

    def llamaInterface(self, l, op):
        self.opc(Interfaz(l), op)

