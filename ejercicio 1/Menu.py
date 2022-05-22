from ManejadorFacultad import ManejadorFacultad

class Menu:
    __Fac=ManejadorFacultad()
    
    def __init__(self):
        self.__Fac= ManejadorFacultad()
        self.__Fac.cargarLista()
        
    
    def Menudeop(self):
        print('1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. \n\n 2. Dado el nombre de una carrera, mostrar código (se conforma con número de código, nombre y localidad de la facultad donde esta se dicta.')
        op= int(input('Ingrese una opcion: \n'))
        
        while op!=0:
            if op==1:
                codF= int(input('Ingrese codigo de una facultad: '))
                self.__Fac.Mostrar_Fac(codF)
            elif op==2:
                codC= int(input('Ingrese codigo de una carrera:  '))
                self.__Fac.MostrarCar(codC)
                
                
            print('1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. \n\n 2. Dado el nombre de una carrera, mostrar código (se conforma con número de código, nombre y localidad de la facultad donde esta se dicta.')
            op= int(input('Ingrese una opcion: \n'))
