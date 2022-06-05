from Aparatos import Aparatos
class Heladeras(Aparatos):
    __capacidadLitros: str
    __freezer: bool
    __ciclica: bool

    def __init__(self, marca, modelo, color, pais, precio, capacidad, freezer, ciclica):
        self.__capacidadLitros= capacidad
        self.__freezer= bool(freezer)
        self.__ciclica= bool(ciclica)
        super().__init__(marca, modelo, color, pais, precio)    


    def getTipo(self):
        return 'Heladera'
    
    def getimporteT(self):
        t= self.getprecio()
        if self.__freezer == False:
            t+= t*0.01
        else:
            t+= t*0.5
        if self.__ciclica == True:
            t+= t*0.10
        
        return t 
    def toJson(self):
        dic= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca= self.getmarca(),
                modelo= self.getmodelo(),
                color= self.getcolor(),
                pais= self.getpais(),
                precio= self.getprecio(),
                capacidadL= self.__capacidadLitros,
                freezer= self.__freezer,
                ciclica= self.__ciclica,


            )
        )
        return dic