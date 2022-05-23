from Flores import Flores
import csv
import numpy as np
from numpy import array
class ManejadorFlor:
    __arregloflor: array
    
    def __init__(self):
        self.__arregloflor= self.cargar()
    
    def cargar(self):
        lista=[]
        archivo= open('flores.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            obj= Flores(fila[0], fila[1], fila[2], fila[3])
            lista.append(obj)
        a= np.array(lista)
        return a
    def get_arr(self):
        return self.__arregloflor
    
    def obtenerflor(self, nomf):
        i=0
        band= False
        retorno= -1
        while i<len(self.__arregloflor) and band== False:
            if self.__arregloflor[i].getnom== nomf:
                retorno= self.__arregloflor[i]
                band= True
            else: i+=1
        return retorno
