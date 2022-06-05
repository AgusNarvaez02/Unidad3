class Aparatos:
    __marca: str
    __modelo:str
    __color: str
    __pais:str
    __precioBase:float

    def __init__(self, marca, modelo, color, pais, precio):
        self.__marca= marca
        self.__color= color
        self.__modelo= modelo
        self.__pais= pais
        self.__precioBase=float(precio)
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getcolor(self):
        return self.__color
    def getpais (self):
        return self.__pais
    def getprecio(self):
        return self.__precioBase
