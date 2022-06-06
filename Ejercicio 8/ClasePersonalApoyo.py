from ClasePersonal import Personal
class PersonalApoyo(Personal):
    __categoria: int

    def __init__(self, **kwargs):
        self.__categoria= kwargs['categoria']
        super().__init__(**kwargs)
    
    def getTipoAgente(self):
        return (self.__class__.__name__)

    def gercategP(self):
        return self.__categoria
    def calculosueldo(self):
        t= self.getsueldoBase
        t+= t* self.getanti()/100
        if self.__categoria>= 1 or self.__categoria<=10:
            t+= t*0.10
        elif self.__categoria>= 11 or self.__categoria<=20:
            t+= t*0.20
        elif self.__categoria>= 21 or self.__categoria<=22:
            t+= t*0.30
        self.setsueldo(t)
    def toJson(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil= self.getcuil(),
                apellido= self.getapellido(),
                nombre= self.getnombre(),
                sueldo= self.getsueldoBase(),
                antig= self.getanti(),
                categoria= self.__categoria

            )
        )
        return d