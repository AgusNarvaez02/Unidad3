from Aparatos import Aparatos
class Lavarropas(Aparatos): 
    __capacidad: int
    __velocidad: int
    __cantidad_Programas: int
    __TipoCarga: str

    def __init__(self, marca, modelo, color, pais, precio, capacidad, velocidad, cantP, tipoC):
        self.__capacidad= int(capacidad)
        self.__velocidad= int(velocidad)
        self.__cantidad_Programas= int(cantP)
        self.__TipoCarga= tipoC
        super().__init__(marca, modelo, color, pais, precio)


    def getTipo(self):
        return 'Lavarropa'
    def getTipoCarga(self):
        return self.__TipoCarga
    def getimporteT(self):
        t= self.getprecio()
        if self.__capacidad <= 5:
            t+= t*0.01
        elif self.__capacidad>=5:
            t+= t*0.3
        
        
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
                capacidad= self.__capacidad,
                velocidad = self.__velocidad,
                cantidadP= self.__cantidad_Programas,
                TipoCarga= self.__TipoCarga
            )
        )
        return dic