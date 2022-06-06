from ObjectEncoder import ObjectEncoder
from ClaseDocente import Docente
from CLaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ManejadorInterfaz import ManejadorInterface
from ClaseLista import Lista
class Menu:
    __Clista: Lista

    def __init__(self):
        self.__Clista= Lista()
        try:
            manInterfaz= ManejadorInterface()
            Json= ObjectEncoder()
            Json.decodificadorDiccionario(self.__Clista)
        except:
            print('Debe crerarse el archivo, ingresar a opcion 1\n')
    
    def opciones(self):
        print('1. Crear archivo JSON \n')
        print('2. Insertar a agentes a la colección.\n')
        print('3. Agregar agentes a la colección.\n')
        print('4. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.\n')
        print('5. Generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores. \n')
        print('6. Contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n ')
        print('7. Generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.\n ')
        print('8. Listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría \n')
        print('9. Almacenar los datos de todos los agentes en el archivo “aparatoselectronicos.json” \n')
    
    def cargararchJSON(self,jsonF):
        ob1 = Docente(cuil="20-3454506-8", apellido="Perez", nombre="Nicolas", sueldo=89000, anti=3,carrera="LCC", cargo="JTP", catedra="Sistemas de Informacion")
        ob2 = Investigador(cuil="15-324235-5", apellido="Dominguez", nombre="Juan", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        ob3 = PersonalApoyo(cuil="12-456543-4", apellido="Castro", nombre="Maria", sueldo=140000, anti=2,categoria="I")
        ob4 = DocenteInvestigador(programa="I", importe=25000, cuil="18-3446706-8", apellido="Lopez",nombre="Marcos", sueldo=89000, anti=3, catedra="EyFCI", carrera="LCC",cargo="Jefe de Catedra", area="Estructuras", tipo="Teorica")
        d1 = ob1.toJson()
        d2 = ob2.toJson()
        d3 = ob3.toJson()
        d4 = ob4.toJson()
        lista = [d1, d2, d3, d4]
        jsonF.guardarJSONArchivo(lista, "personal.json")
    
    def Menuop(self):
        manInterfaz= ManejadorInterface()
        Json= ObjectEncoder()
        Json.decodificadorDiccionario(self.__Clista)
        self.opciones()
        op= int(input('Ingrese una opcion distinta de 0: '))
        while op!= 0:
            if op==1:
                self.cargararchJSON(Json)
            elif op==2:
                manInterfaz.llamaInterface(self.__Clista, op)
            elif op== 3:
                manInterfaz.llamaInterface(self.__Clista, op)
            elif op== 4:
                manInterfaz.llamaInterface(self.__Clista, op)
            elif op== 5:
                self.__Clista.ordenarNombre()
            elif op==6:
                area= input('Ingrese un area de investigacion: ')
                self.__Clista.investigadorescont(area)
            
            elif op==7:
                self.__Clista.ordenarApellido()
            
            elif op== 8:
                categoria=input(' Ingrese una categoria: ')
                self.__Clista.Listadocateg(categoria)
            elif op== 9:
                self.__Clista.almacenar(Json)
            self.opciones()
            op= int(input('Ingrese una opcion distinta de 0: '))   

    def MenuDirector(self, user):
        manInterfaz= ManejadorInterface()
        print('a. Modificar sueldo basico \n b. Modificar porcentaje por cargo \n c. Modificar porcentaje por categoria \n d. Modificar importe extra\n')
        op= input('Ingrese una opcion, X para regresar al menu principal o z para finalizar\n')
        while op!= 'z':
            if op== 'a':
                manInterfaz.llamaInterface(self.__Clista, op, user)
            elif op== 'b':
                manInterfaz.llamaInterface(self.__Clista, op, user)
            elif op== 'c':
                manInterfaz.llamaInterface(self.__Clista, op, user)
            elif op== 'd':
                manInterfaz.llamaInterface(self.__Clista, op, user)
            elif op== 'x':
                self.Menuop()
            print('a. Modificar sueldo basico \n b. Modificar porcentaje por cargo \n c. Modificar porcentaje por categoria \n d. Modificar importe extra\n')
            op= input('Ingrese una opcion, X para regresar al menu principal o z para finalizar\n')
    

    def MenuTesorero(self, user):
        manInterfaz= ManejadorInterface()
        print('a. Consultar sueldo\n b. Volver al menu principal\n')
        op= input('Ingrese una opcion, z para finalizar: ')
        while op!= 'z':
            if op=='a':
                manInterfaz.llamaInterface(self.__Clista, op, user)
            elif op== 'x':
                self.Menuop()
            print('a. Consultar sueldo\n b. Volver al menu principal\n')
            op= input('Ingrese una opcion, z para finalizar: ')
            

            
