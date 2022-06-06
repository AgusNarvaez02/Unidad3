from ClaseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula: str
    __calorias: str

    def __init__(self, marca, modelo, matricula, calorias):
        self.__matricula= matricula
        self.__calorias= calorias
        super().__init__(marca, modelo)
    
    def getcalorias(self):
        return self.__calorias
    def gettipoG(self):
        return print('Calefactor a Gas')
    