class Carrera:
    __codigo: int
    __nom: str
    __tipo: str
    __duracion: str
    __titulo: str
    
    def __init__(self, codigo, nom, tipo, duracion,titulo):
        self.__codigo= int(codigo)
        self.__nom=nom
        self.__tipo= tipo
        self.__duracion= duracion
        self.__titulo= titulo
        
    
    def getcodigo(self):
        return self.__codigo
    def getnombre(self):
        return self.__nom
    def gettipo(self):
        return self.__tipo
    def getdur(self):
        return self.__duracion
    def gettit(self):
        return self.__titulo
    
