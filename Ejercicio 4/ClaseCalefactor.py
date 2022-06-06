
class Calefactor:
    __marca: str
    __modelo: str

    def __init__(self, marca, modelo):
        self.__marca= marca
        self.__modelo= modelo
    
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
        