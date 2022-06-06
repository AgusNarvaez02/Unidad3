class Personal:
    __cuil: int
    __apellido= str
    __nombre: str
    __sueldoBase: float
    __antig: str

    def __init__(self, **kwargs):
        self.__cuil= kwargs['cuil']
        self.__apellido= kwargs['apellido']
        self.__nombre= kwargs['nombre']
        self.__sueldoBase= kwargs['sueldo']
        self.__antig= kwargs['antig']
    
    def getcuil(self):
        return self.__cuil
    def getapellido(self):
        return self.__apellido
    
    def getnombre(self):
        return self.__nombre
    def getsueldoBase(self):
        return self.__sueldoBase
    
    def getanti(self):
        return self.__antig
    def setsueldo(self,t):
        self.__sueldoBase= t
    def __gt__(self, otro):
        b= False
        if self.__nombre> otro.__nombre:
            b= True
        return b
    def claculaSueldo(self):
        pass
    