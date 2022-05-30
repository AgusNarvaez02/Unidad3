class Equipo:
    __Nombre: str
    __Ciudad: str
    __contratos=[]
    
    def __init__(self, nom, ciu):
        self.__Nombre= nom
        self.__Ciudad= ciu
        self.__contratos=[] 
    
    def agregarcontrato(self, contr):
        self.__contratos.append(contr)
    
    def getnom(self):
        return self.__Nombre
    
    def getcontrato(self):
        return self.__contratos