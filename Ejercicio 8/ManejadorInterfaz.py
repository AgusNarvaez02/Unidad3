from ClaseInterfaz import Interfaz
from ClaseLista import Lista
from ObjectEncoder import ObjectEncoder
from IDirector import IDirector
from ITesorero import ITesorero
class ManejadorInterface:
    __controladorO= ObjectEncoder
    def __init__(self):
        self.__controladorO= ObjectEncoder()
    def opcgeneral(self, lista: Interfaz, op):
        if op== 2:
            t= input('Ingrese tipo de agente: ')
            ob= self.__controladorO.retornarObj
            p= int(input('Ingrese posicion donde se encuentra el objeto: '))
            if ob != None:
                lista.insertarElemento(p, ob)
            else: 
                print('Objeto incorrecto \n')
        
        elif op== 3:
            t= input('Ingrese tipo de agente: ')
            ob= self.__controladorO.retornarObj()
            if ob!= None:
                lista.insertarFinal(ob)
            else: print('ERROR\n')

        elif op== 4:
            p= int(input('Ingrese alguna posicion de la lista \n'))
            date= lista.tipoObj(p)
            if date != None:
                print('Tipo de dato: {}'.format(date.getTipoAgente))
            
            else: print('Pocision eeronea \n')
        
    def opcDirector(self, lista: IDirector, op):
        if op== 'a':
            c= input('Ingrese CUIL del agente: ')
            im= float(input('Ingrese nuevo sueldo: \n'))
            lista.modificarBasico(c, im)

        elif op== 'b':
            c= input('Ingrese CUIL del agente: ')
            im= float(input('Ingrese nuevo porcentaje: \n'))
            lista.modificarPorcentajeporcargo(c, im)
        elif op== 'c':
            c= input('Ingrese CUIL del agente: ')
            im= float(input('Ingrese nuevo porcentaje para la categoria: \n'))
            lista.modificarBasico(c, im)
        elif op== 'd':
            c= input('Ingrese CUIL del agente: ')
            im= float(input('Ingrese importe extra: \n'))
            lista.modificarBasico(c, im)
        else: print('Opcion erronea')
    
    def opcTesorero(self, lista: ITesorero, op):
        if op== 'a':
            c= input('Ingrese CUIL del agente: ')
            lista.gastosSueldoPorEmpleado(c)
        else: print('Opcion incorrecta\n')
    


    def llamaInterface(self, lista, op, user= 'general'):
        if user.lower()=='general':
            self.opcgeneral(Interfaz(lista), op)
        if user.lower()=='director':
            self.opcDirector(Interfaz(lista), op)
        if user.lower()=='tesorero':
            self.opcTesorero(Interfaz(lista), op)