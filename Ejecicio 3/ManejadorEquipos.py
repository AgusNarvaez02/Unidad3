from Equipo import Equipo
from numpy import ndarray
import numpy as np
import csv

class ManejadorEquipo:
    __arregloequip:ndarray
    
    
    def cargararre(self):
        cont=0
        archivo= open('equipos.csv')
        reader= csv.reader(archivo, delimiter=';')
        tam= next(reader)
        print(tam)
        self.__arregloequip=np.empty(int(tam[0]), dtype=Equipo)
        for fila in reader:
            obj= Equipo(fila[0],fila[1])
            self.__arregloequip[cont]= obj
            cont+=1
    
    def buscar(self,nom):
        i=0
        retorno= -1
        band= False
        while i<len(self.__arregloequip) and band== False:
            if self.__arregloequip[i].getnom()== nom:
                retorno= self.__arregloequip[i]
                band= True
            else: i+=1
        return retorno
    
    def getequipo(self, pos):
        return self.__arregloequip[pos]
    
    def mostrarimporte(self, equipo):
        acum=0
        for elem in equipo.getcontrato():
            acum+= elem.getpago()
    
        return acum

    
        
    