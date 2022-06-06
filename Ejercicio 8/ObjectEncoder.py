from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseLista import Lista
from CLaseDocenteInvestigador import DocenteInvestigador 
from pathlib import Path
import json
class ObjectEncoder(object):
    def decodificadorDiccionario(self, lista: Lista):
        diccionario= self.leerJSONarchivo('Peronal.json')
        for elem in diccionario:
            if '__class__' not in elem:
                print('No se encuentra el diccionario')
            else:
                class_name= elem['__class__']
                class_= eval(class_name)
                if class_name=='Docente':
                    atributos= elem['__atributos__']
                    D= class_(**atributos)
                    lista.insertarFinal(D)
                elif class_name=='Investigador':
                    atributos= elem['__atributos__']
                    I= class_(**atributos)
                    lista.insertarFinal(I)
                elif class_name=='PersonalApoyo':
                    atributos= elem['__atributos__']
                    P= class_(**atributos)
                    lista.insertarFinal(P)
                elif class_name=='DocenteInvestigador':
                    atributos= elem['__atributos__']
                    DI= class_(**atributos)
                    lista.insertarFinal(DI)
    
    def retornarObjeto(self, tipo):
        if tipo == "docente":
            ob = Docente(cuil="15-1823791-2", apellido="Ortiz", nombre="Juan", sueldo=50000, anti=10, carrera="LSI",cargo="exclusivo", catedra="Programacion Orientada a Objetos")
        elif tipo == "investigador":
            ob = Investigador(cuil="20-1923192-3", apellido="Dominguez", nombre="Carlos", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        elif tipo == "personal apoyo":
            ob = PersonalApoyo(cuil="12-456543-4", apellido="Pereyra", nombre="Maria", sueldo=70000, anti=1,categoria=17)
        elif tipo == "docente investigador":
            ob = DocenteInvestigador(programa="II", importe=25000, cuil="18-3446706-8", apellido="Lopez", nombre="Juan Cruz", sueldo=90000, anti=4, catedra="EyFCI", carrera="LCC",cargo="semiexclusivo", area="Estructuras", tipo="Teorica")
        else:
            ob = None

        return ob

    def guardarJSONarchivo(self, diccionario, archivo):
        with Path(archivo).open("w",encoding= 'UTF-8') as destino:
            json.dump(diccionario, destino, ident=4)
            destino.close()
    

    def leerJSONarchivo(self, archivo):
        with Path(archivo).open(encoding= 'UTF-8') as fuente:
            diccionario= json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoaDiccionario(self, texto):
        return json.loads(texto)
