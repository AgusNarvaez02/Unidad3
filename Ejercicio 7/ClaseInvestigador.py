from ClasePersonal import Personal
class Investigador(Personal):
    __area: str
    __tipo: str

    def __init__(self, **kwargs):
        self.__area= kwargs['area']
        self.__tipo= kwargs['tipo']
        super().__init__(**kwargs)
    
    def getTipoAgente(self):
        return (self.__class__.__name__)
    def getarea(self):
        return self.__area
    def gettipo(self):
        return self.__tipo
    def calculoSueldo(self):
        t= self.getsueldoBase()
        t+= (t*self.getanti()/100)
        self.setsuelddo(t)
    def toJson(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil= self.getcuil(),
                apellido= self.getapellido(),
                nombre= self.getnombre(),
                sueldo= self.getsueldoBase(),
                antig= self.getanti(),
                
                area= self.__area,
                tipo= self.__tipo

            )
        )
        return d