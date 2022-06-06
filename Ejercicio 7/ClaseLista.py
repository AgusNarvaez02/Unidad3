from Nodo import Nodo
from ObjectEncoder import ObjectEncoder
from CLaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from zope.interface import implementer
from ClaseInterfaz import Interfaz
@implementer(Interfaz)
class Lista:
    __comienzo= None
    __actual= None
    __indice= 0
    __tope=0

    def __init__(self):
        self.__comienzo= None
        self.__actual= None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice== self.__tope:
            self.__actual= self.__comienzo
            self.__indice=0
            raise StopIteration
        
        else: 
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual= self.__actual.getSiguiente()
            return dato
    
    def agregar(self, aparato):
        nodo= Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__actual= nodo
        self.__tope+=1
    
    def insertarElem(self, p, obj):
        cont=1
        cabeza= self.__comienzo
        if self.__comienzo is None:
            nodo= Nodo(obj)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo= nodo
            self.__actual= nodo
            self.__tope+=1
        else:
            while cont<p -1 and cabeza is not None:
                cont+=1
                cabeza= cabeza.getSiguiente()
            if p==1:
                nuevoN= Nodo(obj)
                nuevoN.setSiguiente(cabeza)
                self.__comienzo= nuevoN
                self.__actual= nuevoN
            else:
                nuevoN= Nodo(obj)
                nuevoN.setSiguiente(cabeza.getSiguiente())
                cabeza.setSiguiente(nuevoN)
            self.__tope+=1

    def insertarFinal(self, obj):
        if self.__comienzo is None: 
            nodo= Nodo(obj)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo= nodo                    self.__actual= nodo
        else: 
            cabeza= self.__comienzo    
            while cabeza.getSiguiente() is not None:
                cabeza= cabeza.getSiguiente()                    nodo= Nodo(obj)
                cabeza.setSiguiente(nodo)
        self.__tope+=1
            
    def tipodeObjeto(self, pos):
        dato = None
        cont = 1
        if self.__comienzo is None and pos != 1:
            dato = None
        cabeza = self.__comienzo
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()
        return dato
            
    
    def almacenar(self, objE):
        lista=[]
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            dic= dato.toJson()
            lista.append(dic)
            cabeza= cabeza.getSiguiente()
        objE.guardarJSONarchivo(lista,'NuevosAparatos.json')

    def ordenarNombre(self):
        n= input('Ingrese Nombre de la carrera')
        lista= []
        cabeza= self.__comienzo
        while cabeza is not None:
            date= cabeza.getDato()
            if type(date) is DocenteInvestigador:
                if date.getcarrera().lower()== n.lower()
                    lista.append(date)
            cabeza= cabeza.getSiguiente()
        lista= sorted(lista)
        for elem in lista:
            print('Nomre: {}, Aoellido: {}, Carrera: {}'.format(elem.getnombre(), elem.getapellido(), elem.getcarrrera()))
    
    def investigadorescont(self, area):
        c1=0
        c2=0
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            if type(dato) is DocenteInvestigador:
                if dato.getarea().lower()== area.lower():
                    c1+=1
            elif type(dato) is Investigador:
                if dato.getarea().lower()== area.lower():
                    c2+=1
            cabeza= cabeza.getSiguiente()
        print(' Para el area: {} la cantidad de docentes de investigacion es: {} y la cantidad de investigadores es: {}'.format(area, c1, c2))

    def ordenarApellido(self):
        lista= []
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            lista.append(dato)
            cabeza= cabeza.getSiguiente()
        listaord= sorted(lista)
        for elem in listaord
        print('Nombre y apellido: {} {} Tipo de agente: {}, sueldo:{}'.format(elem.getnombre(), elem.getapellido(), elem.getsueldoBase(), elem.gettipo))
    
    def Listadocateg(self, categoria):
        t=0
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            if type(dato) is DocenteInvestigador and dato.getcategoriaProg().lower()== categoria:
                print(dato.getnombre(), dato.getapellido(), dato.getimporte() )
                t+=dato.getimporte() 
            cabeza= cabeza.getSiguiente()
        print('Se debera abonat un total de: ${}'.format(t))
        
