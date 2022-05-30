from Contrato import Contrato
import datetime
class ManejadorContrato:
    __Lista=[]
    
    def __init__(self):
        self.__Lista=[]
    
    def agregarcontrato(self, jug, equip):
        inicio= input('Ingrese fecha de inicio: ')
        fin= input('Ingrese fecha de fin: ')
        pago=input('Ingrese pago mensual: ')
            
        obj= Contrato(inicio, fin, pago, jug, equip)
        self.__Lista.append(obj)
    
    def verificar_siex_cont(self, jug, equip):
        ban= False
        retorno= False
        i=0
        while i<len(self.__Lista) and ban== False:
            if self.__Lista[i].getjugador().getnom()== jug.getnom() and self.__Lista[i].getequipo().getnom()== equip.getnom():
                retorno= True
            i+=1
        return retorno
    
    def mostrareq(self, dni):
        i=0
        ban=False
        while i<len(self.__Lista) and ban==False:
            if self.__Lista[i].getjugador().getdni()== dni:
                print("Jugador contratado\n")
                print("Nombre de equipo: {} -- Fecha de finalizacion del contrato: {}".format(self.__Lista[i].getnomequipo(), self.__arrecontrato[i].getfechafin()))
                ban= False
            i+=1
    
    def contratosporvencer(self, equipo):
        en6meses= datetime.timedelta(days=180) + datetime.date.today()
        print(en6meses)

        for contrato in self.__Lista:
            if contrato.getequipo().getnom()== equipo:
                print(contrato.getfechafin())
                if contrato.getfechafin()<= en6meses:
                    print('Nombre: {}, DNI: {}, Ciudad Natal: {}, Pais de origen: {}, Fecha de Nacimiento: {}'.format(contrato.getjugador().getnom(), contrato.getjugador().getdni(), contrato.getjugador()getciudad(),contrato.getjugador().paisorg(), contrato.getjugador().getnac()))
    
    
