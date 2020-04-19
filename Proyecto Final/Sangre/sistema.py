'''
Sistema de Sangre.
By Roger Urrutia

Concepto general, crear un sistema de donacion de sangre en la cual el donante de su informacion y se pueda ver si este es capaz 
de donarle a alguno de los usuarios quwe necesitan donacion. Para eso se realiza una evaluacion de los tipos de sangre que este puede aceptar.
'''

from collections import defaultdict 
# import pdb
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

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

#Funciones 
def menu():
    print("\nBienvenido a el sistema de Donacion de Sangre. Elige la accion que deseas realizar.\n1.Añadir Donante de Sangre\n2.Añadir Donatario de Sangre\n3.Revisar lista de Donantes\n4.Revisar Lista de Donatarios\n5.Realizar una transfusion\n6.Estadisticas\n7.Salir")
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
        
        opc=menu()
        
        if opc==1:
            cont=1
            while cont==1:
                print(f"Excelente, crearemos un nuevo donante de sangre. Actualmente hay {len(donantes)} donantes de Sangre.")
                name=input("Ingrese el nombre del donante: ")
                age=input("Ingrese la edad del donante: ")
                b_type=input("Ingrese el tipo de sangre del donante: ")
                sex=input("Ingrese el sexo del donante: ")
                sexoDonante[sex]+=1
                try:
                    donantes.append(Donante(name,age,b_type,sex))
                except:
                    print("Parece ser que hubo algun error al momento de añadir al donante. Intenta Nuevamente.")
                else:
                    print("Donador añadido de manera exitosa.")
                cont=input("Desea añadir un nuevo donante? (si/no): ")
                if cont.lower()=="si":
                    cont=1
                else:
                    cont=0
        
        elif opc==2:
            cont=1
            print(f"Excelente, crearemos un nuevo donatario de sangre. Actualmente hay {len(donatarios)} donatarios de Sangre.")
            while cont==1:
                name=input("Ingrese el nombre del donatario: ")
                try:
                    age=int(input("Ingrese la edad del donatario: "))
                except:
                    print("El valor introducido no es una edad. Comenzaremos nuevamente.")
                    break
                else:
                    if age<15:
                        print("Esta Persona es muy joven, no puede donar. Intentar añadir a otra persona.")
                        break
                b_type=input("Ingrese el tipo de sangre del donatario: ")
                if b_type.upper() not in ["A+","B+","O+","AB+","A-","B-","O-","AB-"]:
                    print("Sangre Invalida. Intente Nuevamente.")
                    break
                sex=input("Ingrese el sexo del donatario: ")
                sexoDonatario[sex]+=1
                try:
                    donatarios.append(Donatario(name,age,b_type,sex))
                except:
                    print("Parece ser que hubo algun error al momento de añadir al donatario. Intenta Nuevamente.")
                else:
                    print("Donatario añadido de manera exitosa.")
                cont=input("Desea añadir un nuevo Donatario? (si/no): ")
                if cont.lower()=="si":
                    cont=1
                else:
                    cont=0
        
        elif opc==3:
            if len(donantes)>=1:
                print("Los donantes disponibles son: ")
                for donante in donantes:
                    print(f"\n{donante.name} con sangre tipo {donante.b_type}")
                    sangreDonante[donante.b_type]+=1
                print("\n"+("x"*20))
                for k,v in sangre.items():
                    print(f"\nDe tipo de sangre {k} hay {v} personas.")
                print("\n"+("x"*20))
            else:
                print("\n"+("x"*20))
                print("\nNo hay ningun donante en la base de datos.")
                print("\n"+("x"*20))
        
        elif opc==4:
            if len(donatarios)>=1:
                print("Los donatarios disponibles son: ")
                for donatario in donatarios:
                    print(f"\n{donatario.name} con sangre tipo {donatario.b_type}")
                    sangreDonatario[donatario.b_type]+=1
                print("\n"+("x"*20))
                for k,v in sangre.items():
                    print(f"\nDe tipo de sangre {k} hay {v} personas.")
                print("\n"+("x"*20))
            else:
                print("\n"+("x"*20))
                print("\nNo hay ningun donante en la base de datos.")
                print("\n"+("x"*20))

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
                
                print("Buscando pacientes en la base de datos.")

                if paciente_1.b_type in paciente_2.posible():
                    print(f"El donante {paciente_1.name} puede donarle sin problemas a {paciente_2.name}")
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
            choose=int(input("Con gusto te mostramos las estadisticas. Elige las estadisticas que necesitas visualizar.\n1.Donantes\n2.Donatario\n"))
            #Estadisticas Donantes
            if choose==1:
                if len(donantes)>=1:
                    objects=[]
                    performance=[]
                    for k,v in sexoDonante.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Sexo de los donantes")
                    
                    plt.show()
                
                else:
                    print("No hay donantes en la base de Datos.")
            
            elif choose==2:
            #Estadisticas Donatarios
                if len(donatarios)>=1:
                    objects=[]
                    performance=[]
                    for k,v in sexoDonatario.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Sexo de los Donatarios")
                    plt.show()
                
                else:
                    print("No hay donatarios en la base de Datos.")
        
        elif opc==7:
            print("\nGracias por utilizar la aplicacion.")
            break
        
        else:
            print("\n Opcion no valida.")


                







                    