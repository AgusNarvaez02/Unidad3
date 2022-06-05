class Nodo:
    __aparato= None
    __siguiente= None

    def __init__(self, aparato):
        self.__aparato= aparato
        self.__siguiente= None
    
    def setSiguiente(self, sig):
        self.__siguiente= sig
    
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__aparato