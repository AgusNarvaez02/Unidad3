from ClasePersonal import Personal
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str

    def __init__(self, **kwargs):
        self.__carrera= kwargs['carrera']
        self.__cargo= kwargs['cargo']
        self.__catedra= kwargs['catedra']
        super().__init__(**kwargs)
    
    def getTipoAgente(self):
        return (self.__class__.__name__)
    
    def getcarrera(self):
        return self.__carrera
    
    def getcargo(self):
        return self.__cargo
    
    def getcatedra(self):
        return self.__catedra
    def Sueldo(self):
        t= self.getsueldoBase()
        t=t+ (t*self.getanti()/100)
        if self.__cargo== 'simple':
            t+=(t*0.10)
        elif self.__cargo== 'semiexclusivo':
            t+=(t*0.20)
        elif self.__cargo== 'exclusivo':
            t+=(t*0.30)
        self.setsueldo(t)
    def getsueldoDoc(self):
        return self.getsueldoBase()
    def toJson(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil= self.getcuil(),
                apellido= self.getapellido(),
                nombre= self.getnombre(),
                sueldo= self.getsueldoBase(),
                antig= self.getanti(),
                carrera= self.__carrera,
                cargo= self.__cargo,
                catedra= self.__catedra

            )
        )
        return d   