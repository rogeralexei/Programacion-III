# import pdb
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Funcion para añadir un nuevo donante o donatario
# cont: Se refiere al contador para el bucle en caso de queres agregar mas donantes o donatarios...
# lista: Se refiere a la lista que se usara para almacenar, la de donantes o donatarios...
# donante_donatario: Se refiere a determinar si es un donante o un donatario...
# Con esto, se sabra que se quiere agregar en realidad para evitar repetir...

def nuevo_donante_donatario(cont,lista,donante_o_donatario,sexodict,sangredict):

    
    if len(lista) == 0:
        cantidad = 'no hay'
    else:
        cantidad = f'hay {len(lista)}'

    print(f"Excelente, crearemos un nuevo {donante_o_donatario} de sangre. Actualmente {cantidad} {donante_o_donatario}s de Sangre.")
    while cont==1:
        name=input(f"Ingrese el nombre del {donante_o_donatario}: ")
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

        try:
            if donante_o_donatario == 'donante':
                lista.append(Donante(name,age,b_type,sex))
            else:
                lista.append(Donatario(name,age,b_type,sex))
        except:
            print(f"Parece ser que hubo algun error al momento de añadir al {donante_o_donatario}. Intenta Nuevamente.")
        else:
            print(f"{donante_o_donatario} añadido de manera exitosa.")
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
    if len(lista)>=1:
        print(f"Los {donante_donatario}s disponibles son: ")
        for persona in lista:
            print(f"\n{persona.name} con sangre tipo {persona.b_type}")
        print("\n"+("x"*20))
        for k,v in sangredict.items():
            print(f"\nDe tipo de sangre {k} hay {v} personas.")
        print("\n"+("x"*20))
    else:
        print("\n"+("x"*20))
        print(f"\nNo hay ningun {donante_donatario} en la base de datos.")
        print("\n"+("x"*20))

# Funcion para mostrar las estadisticas de la base de datos de los donantes o donatarios...
# lista: Se refiera a la lista con la cual trabajar...
# sexodict: Base de datos del sexo de los donantes o donatarios
# sangredict: Base de datos de la sangre de los donantes o donatarios
def estadisticas_donantes_donatarios(lista, sexodict, sangredict):
                
    if len(lista)>=1:
        objects=[]
        performance=[]
        for k,v in sexodict.items():
            objects.append(k)
            performance.append(v)
        
        objects=tuple(objects)
        y_pos=np.arange(len(objects))

        plt.bar(y_pos,performance, align="center", alpha=0.5)
        plt.xticks(y_pos,objects)
        plt.ylabel("Cantidad de personas")
        plt.title("Sexo de los donantes")
        
        plt.show()

        objects=[]
        performance=[]
        for k,v in sangredict.items():
            objects.append(k)
            performance.append(v)
        
        objects=tuple(objects)
        y_pos=np.arange(len(objects))

        plt.bar(y_pos,performance, align="center", alpha=0.5)
        plt.xticks(y_pos,objects)
        plt.ylabel("Cantidad de personas")
        plt.title("Tipo de Sangre de los donantes")
        
        plt.show()

    else:
        print("No hay donantes en la base de Datos.")