class Jugador:
    __Nombre: str
    __dni: str
    __ciudad: str
    __Porig: str
    __Fechanac: str
    __contrato=None
    
    def __init__(self, nom, dni, ciudad, Porig, Fechanac):
        self.__Nombre= nom
        self.__dni= dni
        self.__ciudad= ciudad
        self.__Porig= Porig
        self.__Fechanac= Fechanac
        self.__contrato=[]
        
    def agregarcontrato(self, contr):
        self.__contrato.append(contr)
    def getcontrato(self):
        return self.__contrato
        
    
    
    def getnom(self):
        return self.__Nombre
    def getdni(self):
        return self.__dni
    def getorg(self):
        return self.__Porig
    def getciudad(self):
        return self.__ciudad
    def getnac(self):
        return self.__Fechanac
        