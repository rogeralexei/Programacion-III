'''
Sistema de Sangre.
By Roger Urrutia, Hernan Dominguez +Agregar el nombre del resto de los Integrantes

Concepto general, crear un sistema de donacion de sangre en la cual el donante de su informacion y se pueda ver si este es capaz 
de donarle a alguno de los usuarios quwe necesitan donacion. Para eso se realiza una evaluacion de los tipos de sangre que este puede aceptar.
'''

from collections import defaultdict 
# importando las funciones...-Adrien
from funciones import estadisticas_donantes_donatarios,nuevo_donante_donatario,lista_donante_donatario
#Clases
class Donante():

    def __init__(self,name,age,b_type,sex):
        self.name=name
        self.age=age
        self.b_type=b_type
        self.sex=sex


class Donatario(Donante):

    def __init__(self,name,age,b_type,sex):
        super().__init__(name,age,b_type,sex)

    def posible(self):
        if self.b_type=="A+":
            sangre_permitida=["A+","A-","O+","O-"]
        elif self.b_type=="O+":
            sangre_permitida=["O+","O-"]
        elif self.b_type=="B+":
            sangre_permitida=["B+","B-","O+","O-"]
        elif self.b_type=="AB+":
            sangre_permitida=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
        elif self.b_type=="A-":
            sangre_permitida=["A-","O-"]
        elif self.b_type=="O-":
            sangre_permitida=["O-"]
        elif self.b_type=="B-":
            sangre_permitida=["B-","O-"]
        elif self.b_type=="AB-":
            sangre_permitida=["A-","B-","O-","AB-"]
        else:
            return f"La Sangre {self.b_type} no existe."
        return sangre_permitida

def menu():
    print("\nElige la accion que deseas realizar.\n1.Añadir Donante de Sangre\n2.Añadir Donatario de Sangre\n3.Revisar lista de Donantes\n4.Revisar Lista de Donatarios\n5.Realizar una transfusion\n6.Estadisticas\n7.Salir")
    opc=int(input("Seleccionar: "))
    return opc

if __name__=="__main__":
    
    
    donantes=[]
    donatarios=[]
    sexoDonante=defaultdict(lambda:0)
    sexoDonatario=defaultdict(lambda:0)
    sangreDonante=defaultdict(lambda: 0)
    sangreDonatario=defaultdict(lambda: 0)
    
    while True:

        print('Bienvenido a el sistema de Donacion de Sangre.' )
        opc=menu()
        
        if opc==1:
            nuevo_donante_donatario(1,donantes,'donante',sexoDonante,sangreDonante)
        
        elif opc==2:
            
            nuevo_donante_donatario(1,donatarios,'donatario',sexoDonatario,sangreDonatario)

        
        elif opc==3:
           
            lista_donante_donatario(donantes,'donante',sangreDonante)

        elif opc==4:
            
            lista_donante_donatario(donatarios,'donatarios',sangreDonatario)

        elif opc==5:
            
            print("\nSe realizara una transfusion. Es importante que los pacientes se encuentren en la base de datos.")
            
            while True:
                paciente_1=input("\nIngrese el nombre del donante o escriba q para salir: ")
                
                if paciente_1.lower()=="q":
                    break

                for donante in donantes:
                    if donante.name==paciente_1:
                        print("Donante encontrado.")
                        paciente_1=donante
                    else:
                        continue
                
                if paciente_1 not in donantes:
                    print("\nError")
                    break

                paciente_2=input("\nIngrese el nombre del donatario o escriba q para salir: ")
                
                if paciente_2.lower()=="q":
                    break

                for donatario in donatarios:
                    if donatario.name==paciente_2:
                        print("Donatario encontrado.")
                        paciente_2=donatario
                    else:
                        continue
                
                if paciente_2 not in donatarios:
                    print("\nError")
                    break

                if paciente_1.b_type in paciente_2.posible():
                    if paciente_1.sex.lower()=="femenino":
                        articulo="La"
                    else:
                        articulo="El"
                    print(f"{articulo} donante {paciente_1.name} puede donarle sin problemas a {paciente_2.name}")
                    index=donatarios.index(paciente_2)
                    delete=donatarios.pop(index)
                    print(f"{delete.name} ha sido removido de la lista de donatarios!")
                else:
                    print(f"Este donante {paciente_1.name} no puede donarle a {paciente_2.name}")
                    break
                
                continuar=input("Deseas continuar?(si/no): ")
                if continuar.lower()=="si":
                    continue
                else:
                    break
            
        elif opc==6:
            choose=int(input("Con gusto te mostramos las estadisticas. Elige las estadisticas que necesitas visualizar.\n1.Donantes\n2.Donatarios\nSeleccionar:"))
            
            if choose==1:

                estadisticas_donantes_donatarios(donantes,sexoDonatario,sangreDonatario)

            elif choose==2:
            #Estadisticas Donatarios
                estadisticas_donantes_donatarios(donatarios,sexoDonatario,sangreDonatario)
        
        elif opc==7:
            print("\nGracias por utilizar la aplicacion.")
            break
        
        else:
            print("\n Opcion no valida.")


                







                    