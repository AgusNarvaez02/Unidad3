from ClaseDocente import Docente
from ClaseInvestigador import Investigador 
class DocenteInvestigador(Docente, Investigador):
    __categoriaProg: str
    __ImporteE: float

    def __init__(self, **kwargs):
        self.__categoriaProg= kwargs['categoriaP']
        self.__ImporteE= kwargs['ImporteE']
        super().__init__(**kwargs)
    
    def getTipoAgente(self):
        return (self.__class__.__name__)
    def getcategoriaProg(self):
        return self.__categoriaProg
    def getimporte(self):
        return self.__ImporteE
    def calculaSueldo(self):
        total = self.getsueldoDoc()
        total += self.__ImporteE
        self.setsueldo(total)
    def toJson(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil= self.getcuil(),
                apellido= self.getapellido(),
                nombre= self.getnombre(),
                sueldo= self.getsueldoBase(),
                antig= self.getanti(),
                carrera= self.getcarrera(),
                catedra= self.getcatedra(),
                area= self.getarea(),
                tipo= self.gettipo(),
                programa= self.__categoriaProg,
                importe= self.__ImporteE

            )
        )
        return d