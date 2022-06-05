from Aparatos import Aparatos
class Televisores(Aparatos):
    __tipoPantalla: str
    __pulgadas: str
    __tipoDef: str
    __conexion: bool

    def __init__(self, marca, modelo, color, pais, precio, tipoP, pulgadas, tipoD, conexion):
        self.__tipoPantalla= tipoP
        self.__pulgadas= pulgadas
        self.__tipoDef= tipoD
        self.__conexion= bool(conexion)

        super().__init__(marca, modelo, color, pais, precio)
    def getTipo(self):
        return 'Televisor'
    

    def getimporteT(self):
        t= self.getprecio()
        if self.__tipoDef.lower() == 'sd':
            t+= t*0.01
        if self.__tipoDef.lower() == 'hd':
            t+= t*0.02
        if self.__tipoDef.lower() == 'full hd':
            t+= t*0.03
        if self.__conexion == True:
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
                tipoPantalla= self.__tipoPantalla,
                pulgadas= self.__pulgadas,
                TipoDef= self.__tipoDef,
                conexion= self.__conexion


            )
        )
        return dic


