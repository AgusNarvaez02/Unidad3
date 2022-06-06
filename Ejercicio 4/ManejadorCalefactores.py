from ClaseCalefactor import Calefactor
from ClaseCalefactorElectrico import CalefactorElectrico
from ClaseCalefactorGas import CalefactorGas
import csv
import numpy as np
from numpy import array

class ManejadorCalefactores:
    __calefactores: array
    def __init__(self):
        self.__calefactores= np.empty(0, dtype= Calefactor)
    
    def agregarCalefactor(self, calefactor):
        self.__calefactores= np.array(self.__calefactores, calefactor)
    
    def cargarCelectrico(self):
        with open('calefactorelectrico.csv', 'r', encoding= "utf8") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader, None)
            for fila in reader:
                C= CalefactorElectrico(fila[0],fila[1],fila[2])
                self.agregarCalefactor(C)
            archivo.close()
    
    def cargarCgas(self):
        with open('calefactor-a-gas.csv', 'r', encoding= "utf8") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader, None)
            for fila in reader:
                C= CalefactorGas(fila[0],fila[1],fila[2],fila[3])
                self.agregarCalefactor(C)
            archivo.close()
    
    def mingas(self, c, h):
        pos=-1
        min= 9999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores) is CalefactorGas:
                cost= (self.__calefactores[i].getcalorias()/1000)*c*h
                if cost<min:
                    min=cost
                    p=i

        print("El calefactor a gas de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[pos].getmarca(),self.__calefactores[pos].getmodelo()))
        
    def minelectrico(self, c, h):
        pos=-1
        min= 9999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores) is CalefactorElectrico:
                cost=(self.__calefactores[i].getpotencia()/1000)*c*h
                if cost<min:
                    min=cost
                    p=i

        print("El calefactor electrio de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[pos].getmarca(),self.__calefactores[pos].getmodelo()))
    
    def item_3(self,c,h):
        pos1=-1
        pos2=-1
        min1=9999999
        min2=9999999
        costo1=None
        costo2=None
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorElectrico:
                costo1=(self.__calefactores[i].getpotencia()/1000)*c*h
                if costo1 < min1:
                    min1=costo1
                    pos1=i
            elif type(self.__calefactores[i]) is CalefactorGas:
                costo2 = (self.__calefactores[i].getalorias() / 1000) * c * h
                if costo2 < min2:
                    min2 = costo2
                    pos2 = i
        if costo1 < costo2:
            print("Tipo: {}, Calefactor: {}".format(self.__calefactores[pos1].gettipoE(),self.__calefactores[pos1]))
        else:
            print("Tipo: {}, Calefactor: {}".format(self.__calefactores[pos2].gettipoG(), self.__calefactores[pos2]))