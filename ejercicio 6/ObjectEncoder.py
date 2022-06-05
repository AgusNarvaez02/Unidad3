from Heladeras import Heladeras
from Lavarropas import Lavarropas
from Televisores import Televisores
from ClaseLista import Lista 
from pathlib import Path
import json
class ObjectEncoder(object):
    def decodificadorDiccionario(self, lista: Lista):
        diccionario= self.leerJSONarchivo('Aparatos.json')
        for elem in diccionario:
            if '__class__' not in elem:
                print('No se encuentra el diccionario')
            else:
                class_name= elem['__class__']
                class_= eval(class_name)
                if class_name=='Heladeras':
                    atributos= elem['__atributos__']
                    H= class_(**atributos)
                    lista.agregar(H)
                elif class_name=='Televisores':
                    atributos= elem['__atributos__']
                    T= class_(**atributos)
                    lista.agregar(T)
                if class_name=='Lavarropas':
                    atributos= elem['__atributos__']
                    L= class_(**atributos)
                    lista.agregar(L)
    
    def retornarObj(self):
        Ob = None
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        color = input("Ingrese el color: ")
        pais = input("Ingrese el pais: ")
        precio = input("Ingrese el precio: ")
        tipo = input("Ingrese el tipo de aparato (Televisor-Heladera-Lavarropa): ")
        if tipo == "Heladera":
            capacidad = input("Ingrese capacidad: ")
            freezer = input("Ingrese si posee freezer (True o False): ")
            cicl = input("Ingrese si posee ciclica (True o False): ")
            Ob = Heladeras(marca, modelo, color, pais, precio, capacidad, freezer, cicl)
        elif tipo == "Televisor":
            tipo_pant = input("Ingrese tipo de pantalla((crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch)): ")
            pulgad = input("Ingrese las pulgadas: ")
            tipo_def = input("Ingrese el tipo de definicion (SD,HD,FULL HD): ")
            conexion = input("Ingrese si posee conexion a internet (True o False): ")
            Ob = Televisores(marca, modelo, color, pais, precio, tipo_pant, pulgad, tipo_def, conexion)
        elif tipo == "Lavarropa":
            capacidad = input("Ingrese la capacidad en Kg: ")
            velocidad = input("Ingrese la velocidad de centrifugado: ")
            ct = input("Ingrese la cantidad de programas: ")
            tipo = input("Ingrese el tipo de carga(Frontal o Superior): ")
            Ob = Lavarropas(marca, modelo, color, pais, precio, capacidad, velocidad, ct, tipo)
        return Ob

    def guardarJSONarchivo(self, diccionario, archivo):
        with Path(archivo).open('w'encoding= 'UTF-8') as destino:
            json.dump(diccionario, destino, ident=4)
            destino.close()
    

    def leerJSONarchivo(self, archivo):
        with Path(archivo).open(encoding= 'UTF-8') as fuente:
            diccionario= json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoaDiccionario(self, texto):
        return json.loads(texto)