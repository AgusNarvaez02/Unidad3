from ManejadorRamos import ManejadorRamo
class Menu:
    __Ramos= ManejadorRamo()
    
    def __init__(self):
        self.__Ramos= ManejadorRamo()
        
        
    def Menuop(self):
        print('1.Registrar Ramos vendidos\n 2.Mostrar el nombre de las 5 flores  más pedidas en un ramo\n 3. Mostrar las flores vendidas  ')
        op= int(input('Ingrese una opcion'))
        while op!= 0:
            if op== 1:
                self.__Ramos.ventaRamo()
            
            elif op==2:
                self.__Ramos.masvendidos()
            
            elif op==3:
                tipo= input('Ingrese un tipo de ramo')
                self.__Ramos.mostrar(tipo)
            print('1.Registrar Ramos vendidos\n 2.Mostrar el nombre de las 5 flores  más pedidas en un ramo\n 3. Mostrar las flores vendidas  ')
            op= int(input('Ingrese una opcion'))
