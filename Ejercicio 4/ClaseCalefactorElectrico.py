from ClaseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potencia: int

    def __init__(self, potencia, marca, modelo):
        self.__potencia= int(potencia)
        super().__init__(marca, modelo)

    def getpotencia(self):
        return self.__potencia
    def gettipoE(self):
        return print('Calefactor Electrico')