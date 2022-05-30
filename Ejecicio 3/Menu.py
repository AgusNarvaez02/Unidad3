from ManejadorEquipos import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from ManejadorContrato import ManejadorContrato
class Menu:
    __Manjug= ManejadorJugador()
    __Manequip= ManejadorEquipo()
    __Mancon= ManejadorContrato()
    def __init__(self):
        self.__Manjug= ManejadorJugador()
        self.__Manjug.cargarlista()
        self.__Manequip= ManejadorEquipo()
        self.__Manequip.cargararre()
        self.__Mancon= ManejadorContrato()
        
    def op2(self):
        dni= input('Ingrese DNI de jugador: ')
        jugador= self.__Manjug.buscarDNI(dni)
        if jugador!=-1:
            contratos= jugador.getcontrato()
            print(contratos)
            for elem in contratos:
                print('Nombre de equipo:{} '.format(elem.getequipo().getnom()))
        
            
    def opMenu(self):
        
        op=int(input('Ingrese una opcion: '))
    
        while op!=0:
           if op== 1:
               nombre_jugador= input('Ingrese nombre de jugador: ')
               equip= input('Ingrese nombre de equipo: ')
               jugador= self.__Manjug.buscar(nombre_jugador)
               equipo= self.__Manequip.buscar(equip)
               print(jugador, equipo)
               if jugador!=-1 and equipo!=-1:
                   if not self.__Mancon.verificar_siex_cont(jugador, equipo):
                       self.__Mancon.agregarcontrato(jugador, equipo)
                       print('Se creo el contrato')
                   else:
                       print('El jugador con el Equipo ya poseen un contrato')
           if op==2:
               self.op2()
            if op==3:
                identificador= input('Ingrese nombre de un equipo: ')
                Nombre_equipo= self.__Manequip.buscar()
                

           op=int(input('Ingrese una opcion: '))
        
               
                