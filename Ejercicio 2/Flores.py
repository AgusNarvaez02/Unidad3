class Flores:
    __numero: int
    __Nombre: str
    __color: str
    __descr: str
    
    def __init__(self, Numero, Nombre, color, descr):
        self.__numero= int(Numero)
        self.__Nombre= Nombre
        self.__color= color
        self.__descr= descr
    
    def getnum(self):
        return self.__numero
    def getnom(self):
        return self.__Nombre
    def getcolor(self):
        return self.__color
    def getdescr(self):
        return self.__descr
        
