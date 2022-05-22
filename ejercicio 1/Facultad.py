from Carrera import Carrera
class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: int
    __ListaCarrera=[Carrera]
    
    
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo= codigo
        self.__nombre= nombre
        self.__direccion= direccion
        self.__localidad= localidad
        self.__telefono= telefono
        self.__ListaCarrera= []  
        
        
    def agregarcar(self, i):
        self.__ListaCarrera.append(i)
    
    def getcod(self):
        return self.__codigo
    def getnom(self):
        return self.__nombre
    def getdirec(self):
        return self.__direccion
    def getloc(self):
        return self.__localidad
    def gettel(self):
        return self.__telefono
    
    def getlong(self):
        return len(self.__ListaCarrera)
    
    def getnomCar(self, j):
        return self.__ListaCarrera[j].getnombre()
    def getdurCar(self, j):
        return self.__ListaCarrera[j].getdur()
    def getcodCar(self, j):
        return self.__ListaCarrera[j].getcodigo()
    
