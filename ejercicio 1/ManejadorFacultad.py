from Facultad import Facultad
from Carrera import Carrera
import csv
class ManejadorFacultad:
    __listaFac=[]
    
    def __init__(self):
        self.__listaFac=[]
    
    def cargarLista(self):
        archivo= open('Facultades.csv')
        reader=csv.reader(archivo, delimiter=',')
        fila= next(reader)
        band= True
        while band:
            filaCar= next(reader)
            obj= Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__listaFac.append(obj)
            while band and fila[0] == filaCar[0]:
                try:
                    car= Carrera(filaCar[1], filaCar[2],filaCar[3],filaCar[4],filaCar[5]) 
                    obj.agregarcar(car)
                    filaCar= next(reader)
                except StopIteration:
                    band= False
            fila=filaCar
        archivo.close()
        
    def Mostrar_Fac(self, codF):
        i=0
        band= False
        while i<len(self.__listaFac) and band ==False:
            print('Estra al while')
            if self.__listaFac[i].getcod() == codF:
                print('Nombre de Facultad: {}' .format(self.__listaFac[i].getnom()))
                for j in range(self.__listaFac[i].getlong()):
                    print('Carrera: {}, Duracion: {}'.format(self.__listaFac[i].getnomCar(j), self.listaFac[i].getdurCar(j)))
                band= True
            else: i+=1
    
    def MostrarCar(self, c):
        i=0
        band= False
        
        while i<len(self.__listaFac) and band== False:
            b= False
            j=0
            
            while j<self.__listaFac[i].getlong() and b== False:
                if self.__listaFac[i].getnomCar(j)== c:
                    print ('Codigo Facultad: {}\n Codigo Carrera: {} \n Nombre de Facultad: {} \n Localidad: {} \n'.format(self.__listaFac[i].getcod(), self.__listaFac[i].getcodCar(j), self.__listaFac[i].getnom(), self.__listaFac[i].getloc()))
                    
                    band= True
                    b= True
                else: j+=1
            
            i+=1
