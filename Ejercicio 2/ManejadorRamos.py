from ManjeadorFlores import ManejadorFlor
from Flores import Flores
from Ramos import Ramos
class ManejadorRamo:
    __listaRamo: None
    __flor= ManejadorFlor()
    
    def __init__(self):
        self.__listaRamo=[Ramos]
        self.__flor= ManejadorFlor()
    
    def ventaRamo(self):
        tam= input('Ingrese tamaño de Ramo= Grande - Mediano- chico')
        
        if tam in ['Grande', 'Mediano', 'Grande']:
            ramo= Ramos(tam)
            band= False
            while ramo.getcantFlor()<4 and band== False:
                nomF= input('Ingrese nombre de flor, Fin para finalizar')
                
                if nomF== 'fin':
                    band= True
                else:
                    f= self.__flor.obtenerflor(nomF)
                
                if f==-1:
                    print('La flor no existe')
                else: ramo.agregarFlor(f)
            self.__listaRamo.append(ramo)
        
        else: print('Tamaño de ramo incorrecto')
    
    def masvendidos(self):
        dic: dict[str, int]={}
        for elem in self.__listaRamo:
            for f in elem.getlista():
                nom= f.getnom()
                if nom in dic:
                    dic[nom]+=1
                else: dic[nom]=1
        lista= sorted(dic.items(), key= lambda y: y[1], reverse=True)
        print('------Las 5 flores mas vendidad------\n')
        i=0
        while i<5 and i<len(lista):
            print(lista[i][0])
            i+=1
    
    def mostrar(self, tip):
        print('Ramo de tamaño: {}'.format(tip))
        
        for elem in self.__listaRamo:
            if elem.gettam() == tip:
                for f in elem.getlista():
                    print('Flores vendidad: {} '.format(f.getnom()))
        
