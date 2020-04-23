'''

Sistema de Sangre.

By 
Roger Urrutia 
Jose L. Gonzalez M.
Ricardo Tejera
Leidys Tello
Himani Budhrani
Uliano Paz
Diego Martinez
Hernan Dominguez



Concepto General, 
crear un sistema de donación de sangre en la cual el donante brinde su información y se pueda ver si este es capaz 
de donarle a alguna de las personas que necesitan donación. Para esto se realiza una evaluación de los tipos de sangre que este puede aceptar.

'''

from collections import defaultdict 

import termcolor
# importando las funciones...-Adrien
import funciones as fn

if __name__=="__main__":
    
    
    donantes=[]
    donatarios=[]
    sexoDonante=defaultdict(lambda:0)
    sexoDonatario=defaultdict(lambda:0)
    sangreDonante=defaultdict(lambda: 0)
    sangreDonatario=defaultdict(lambda: 0)
    
    while True:

        opc=fn.menu()
        
        if opc==1:
            fn.nuevo_donante_donatario(1,donantes,'donante',sexoDonante,sangreDonante)
        
        elif opc==2:
            
            fn.nuevo_donante_donatario(1,donatarios,'donatario',sexoDonatario,sangreDonatario)

        
        elif opc==3:
           
            fn.lista_donante_donatario(donantes,'donante',sangreDonante)

        elif opc==4:
            
            fn.lista_donante_donatario(donatarios,'donatarios',sangreDonatario)

        elif opc==5:
            
            print("\nSe realizara una transfusion. Es importante que los pacientes se encuentren en la base de datos.")
            
            while True:
                nombre=input("\nIngrese el nombre del donante o escriba q para salir: ")
                apellido=input("\nIngrese el apellido del donante o escriba q para salir: ")
                paciente_1=""
                paciente_2=""
                
                if nombre.lower()=="q" or apellido.lower()=="q":
                    break


                for donante in donantes:
                    if (donante.name+donante.apellido).lower()==(nombre+apellido).lower():
                        print("Donante encontrado.")
                        paciente_1=donante
                    else:
                        continue
                
                if paciente_1 not in donantes:
                    print("\nError")
                    break

                nombre_2=input("\nIngrese el nombre del donatario o escriba q para salir: ")
                apellido_2=input("\nIngrese el apellido del donatario o escriba q para salir: ")
                
                if nombre_2.lower()=="q" or apellido_2.lower()=="q":
                    break

                for donatario in donatarios:
                    if (donatario.name+donatario.apellido).lower()==(nombre_2+apellido_2).lower():
                        print("Donatario encontrado.")
                        paciente_2=donatario
                        sangreDonatario[paciente_2.b_type]-=1
                        sexoDonatario[paciente_2.sex]-=1
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
                    print(f"\n{articulo} donante {paciente_1.name} puede donarle sin problemas a {paciente_2.name}")
                    index=donatarios.index(paciente_2)
                    delete=donatarios.pop(index)
                    print(f"{delete.name} ha sido removido de la lista de donatarios!")
                else:
                    print(f"\nEste donante {paciente_1.name} no puede donarle a {paciente_2.name}")
                    break
                
                continuar=input("Deseas realizar otra transfusion?(si/no): ")
                if continuar.lower()=="si":
                    continue
                else:
                    break
            
        elif opc==6:
            choose=int(input("Con gusto te mostramos las estadisticas. Elige las estadisticas que necesitas visualizar.\n1.Donantes\n2.Donatarios\nSeleccionar:"))
            
            if choose==1:

                fn.estadisticas_donantes_donatarios(donantes,sexoDonante,sangreDonante,"donante")

            elif choose==2:
            #Estadisticas Donatarios
                fn.estadisticas_donantes_donatarios(donatarios,sexoDonatario,sangreDonatario,"donatario")
        
        elif opc==7:
            print(termcolor.colored("\nGracias por utilizar la aplicacion. 🚀","red"))
            break
        
        else:
            print("\n Opcion no valida.")






                    