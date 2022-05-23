from Flores import Flores
from typing import Literal
class Ramos:
    __Tamaño: str
    __listFlor= [Flores]
    
    def __init__(self, Tamaño: Literal['Grande', 'Mediano', 'Chico']):
        self.__Tamaño= Tamaño
        self.__listFlor=[]
    
    
    def agregarFlor(self, nom):
        self.__listFlor.append(nom)
    def getcantFlor(self):
        return len(self.__listFlor)
    
    def gettam(self):
        return self.__Tamaño
    def getlista(self):
        return self.__listFlor
