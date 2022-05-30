from Jugador import Jugador
import csv

class ManejadorJugador:
    __listajug= []
    
    def __init__(self):
        self.__listajug= []
    
    def cargarlista(self):
        archivo= open('jugadores.csv')
        reader= csv.reader(archivo, delimiter=';')
        for fila in reader:
            obj= Jugador(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__listajug.append(obj)
        
        archivo.close()
    
    def buscar(self,nom):
        i=0
        retorno= -1
        band= False
        while i<len(self.__listajug) and band== False:
            print(self.__listajug[i].getnom(), nom)
            if self.__listajug[i].getnom()== nom:
                retorno= self.__listajug[i]
                band= True
            else: i+=1
        return retorno
    def getjugador(self, pos):
        return self.__listajug[pos]
    def buscarDNI(self, dni):
        i=0
        retorno= -1
        band= False
        while i<len(self.__listajug) and band== False:
            if self.__listajug[i].getdni()== dni:
                retorno= self.__listajug[i]
                band= True
            else: i+=1
        return retorno
    
    def getcontrato(self):
        pass