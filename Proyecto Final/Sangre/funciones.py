import pdb,os,time

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from classes import Donante, Donatario

def menu():
    """
    Manda el Menú 

    Opciones:

        1: Añadir a un donante

        2: Añadir a un donatario

        3: Revisar la lista de donantes

        4: Revisar la lista de donatarios

        5: Realizar una transfusión

        6: Estadisticas

        7: Salir

    Returns:

        opc(num):Opcion del menu 
    """

    print('Bienvenido a el sistema de Donacion de Sangre.' )
    print("\nElige la accion que deseas realizar.\n1.Añadir Donante de Sangre\n2.Añadir Donatario de Sangre\n3.Revisar lista de Donantes\n4.Revisar Lista de Donatarios\n5.Realizar una transfusion\n6.Estadisticas\n7.Salir")
    opc=int(input("Seleccionar: "))
    return opc

# Funcion para añadir un nuevo donante o donatario
# cont: Se refiere al contador para el bucle en caso de queres agregar mas donantes o donatarios...
# lista: Se refiere a la lista que se usara para almacenar, la de donantes o donatarios...
# donante_donatario: Se refiere a determinar si es un donante o un donatario...
# Con esto, se sabra que se quiere agregar en realidad para evitar repetir...

def nuevo_donante_donatario(cont,lista,donante_o_donatario,sexodict,sangredict):
    while cont==1:
        """

            Ésta condicional trabaja una función donde interesa saber los datos de un nuevo donante 

            Nombre>> str que se almanacena en la "Base de Datos"
            
            Apellido>> str que se almanacena en la "Base de Datos"

            Edad>> tiene una condición que indica si la edad es apta o no para la tarea. 

            Typo de Sangre>> pide datos y llama la funcion b_type() tambien verifica TYPO error. condiciona la variable a esta en un rango en especifico

            ===================

            Llama la lista de donantes y retorna escanarios para el proceso de añadirlos

            Opcion de agregar una nueva tarea 

        """
        os.system('clear')
        print(f"Excelente, crearemos un nuevo {donante_o_donatario} de sangre. Actualmente hay {len(lista)} {donante_o_donatario}s de Sangre.")
        name=input(f"Ingrese el nombre del {donante_o_donatario}: ")
        apellido=input(f"Ingrese el apellido del {donante_o_donatario}: ")
        try:
            age=int(input(f"Ingrese la edad del {donante_o_donatario}: "))
        except:
            print("El valor introducido no es una edad. Comenzaremos nuevamente.")
            break
        else:
            if age<15 and donante_o_donatario == 'donante':
                print("Esta Persona es muy joven, no puede donar. Intentar añadir a otra persona.")
                continue
        b_type=input(f"Ingrese el tipo de sangre del {donante_o_donatario}: ").upper()
        if b_type.upper() not in ["A+","B+","O+","AB+","A-","B-","O-","AB-"]:
            print("Sangre Invalida. Intente Nuevamente.")
            continue
        else:
            
            sangredict[b_type]+=1
            sex=input(f"Ingrese el sexo del {donante_o_donatario}: ")
            sexodict[sex]+=1

        if donante_o_donatario == 'donante':
            try:
                lista.append(Donante(name,apellido,age,b_type,sex))
            except:
                print(f"Parece ser que hubo algun error al momento de añadir al {donante_o_donatario}. Intenta Nuevamente.")
            else:
                print(f"\n{donante_o_donatario.title()} \"{name.title()} {apellido.title()}\" añadido de manera exitosa.")
        else:
            try:
                lista.append(Donatario(name,apellido,age,b_type,sex))
            except:
                print(f"Parece ser que hubo algun error al momento de añadir al {donante_o_donatario}. Intenta Nuevamente.")
            else:
                print(f"\n{donante_o_donatario.title()} \"{name.title()} {apellido.title()}\" añadido de manera exitosa.")
        cont=input(f"Desea añadir un nuevo {donante_o_donatario}? (si/no): ")
        if cont.lower()=="si":
            cont = 1
        else:
            cont = 0

# Funcion para mostrar la lista de donantes o donatarios
# lista: Se refiera a la lista con la cual trabajar...
# donante_donatario: Aqui se define si es 'donante' o 'donatario'
# Esta funcion la hice con estos parametros con el fin de no repetir...-Adrien...

def lista_donante_donatario(lista,donante_donatario,sangredict):
    """

    Abre la lista de donates o donatarios y contabiliza 

    toma el rango de los donates disponibles por cantidad 

    retorna por nombre/tipo de sangre tambien la cantida especifica de un tipo de sangre con su data

            

    """
    if len(lista)>=1:
        print(f"Los {donante_donatario}s disponibles son: ")
        for persona in lista:
            print(f"\n{persona.name} {persona.apellido} con sangre tipo {persona.b_type}")
        print("\n"+("x"*20))
        for k,v in sangredict.items():
            print(f"\nDe tipo de sangre {k} hay {v} personas.")
        print("\n"+("x"*20))
        time.sleep(5)
    else:
        print("\n"+("x"*20))
        print(f"\nNo hay ningun {donante_donatario} en la base de datos.")
        print("\n"+("x"*20))
        time.sleep(5)

# Funcion para mostrar las estadisticas de la base de datos de los donantes o donatarios...
# lista: Se refiera a la lista con la cual trabajar...
# sexodict: Base de datos del sexo de los donantes o donatarios
# sangredict: Base de datos de la sangre de los donantes o donatarios

def estadisticas_donantes_donatarios(lista, sexodict, sangredict,tipo):
    """

    Toma el rango de la Lista de los donantes se agregan axis de objects/ performance

    se genera una gráfica mostrandado la data activa de los donantes

    """
    if len(lista)>=1:
        objects=[]
        performance=[]
        for k,v in sexodict.items():
            objects.append(k)
            performance.append(v)
        
        objects=tuple(objects)
        y_pos=np.arange(len(objects))

        plt.bar(y_pos,performance, align="center", alpha=1)
        plt.xticks(y_pos,objects)
        plt.ylabel("Cantidad de personas")
        plt.title(f"Sexo de los {tipo}s")
        
        plt.show()

        objects=[]
        performance=[]
        for k,v in sangredict.items():
            objects.append(k)
            performance.append(v)
        
        objects=tuple(objects)
        y_pos=np.arange(len(objects))

        plt.bar(y_pos,performance, align="center", alpha=1)
        plt.xticks(y_pos,objects)
        plt.ylabel("Cantidad de personas")
        plt.title(f"Tipo de Sangre de los {tipo}s")
        
        plt.show()

    else:
        print(f"No hay {tipo}s en la base de Datos.")