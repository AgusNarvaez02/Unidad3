from Nodo import Nodo
from ObjectEncoder import ObjectEncoder
from zope.interface import implementer
from Interfaz import Interfaz
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
            
    def tipoObj(self, p):
        
        dato= None
        c=1
        if self.__comienzo in None and p!=1:
            dato= None
            cabeza= self.__comienzo
        while cabeza.getSiguiente() is None and c<p:
            c+=1
            cabeza= cabeza.getSiguiente()
        if c== p:
            dato= cabeza.getDato()
            
            return dato 
            
    def ctPhil(self):
        c=0
        cabeza= self._comienzo
        while cabeza is not None :
            dato= cabeza.getDato()
            if dato.getMarca().lower()== 'phillips':
                c+=1
            cabeza= cabeza.getSiguiente()
        return c

    def superior(self):
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            if dato.getTipo().lower()== 'lavarropa' and dato.getTipoCarga().lower()=='superior':
                print('Marca de lavarropa= {} '.format(dato.getmarca()))
            cabeza= cabeza.getSiguiente()
    
    def MostrarAparatos(self):
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            print('Marca: {}, Pais de fabricacion: {}, Importe e venta: {} '.format(dato.getmarca(), dato.getpais(), dato.getimporteT()))
            cabeza= cabeza.getSiguiente()
    
    def almacenar(self, objE):
        lista=[]
        cabeza= self.__comienzo
        while cabeza is not None:
            dato= cabeza.getDato()
            dic= dato.toJson()
            lista.append(dic)
            cabeza= cabeza.getSiguiente()
        objE.guardarJSONarchivo(lista,'NuevosAparatos.json')

 