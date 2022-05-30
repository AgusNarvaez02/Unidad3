import datetime

def parseDate(str:str):
    return datetime.datetime.strptime(str,'%d/%m/%Y').date()

class Contrato:
    __Pagomen: float
    __jugadores: str
    __equipo: str
    
    def __init__(self, Fini, Ffin, Pagomen, jugador, equipo):
        self.__Fini= parseDate(Fini)
        self.__Ffin= parseDate(Ffin)
        self.__Pagomen= Pagomen
        self.__jugadores= jugador
        self.__equipo= equipo
        jugador.agregarcontrato(self)
        equipo.agregarcontrato(self)
        print(jugador)
    def getjugador(self):
        return self.__jugadores
    def getequipo(self):
        return self.__equipo
    def getfechainicio(self):
        return self.__Fini
    def getfechafin(self):
        return self.__Ffin
    def getpago(self):
        return self.__Pagomen
    