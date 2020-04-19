'''
Este programa permite al usuario validar un nombre o una lista de nombres
'''
import pdb

def instrucciones(): #Instrucciones
    print("El siguiente sistema validara si el nombre introducido no se encuentra en la lista de nombres prohibidos del sistema. Nota: Tampoco aceptamos numeros, por que los numeros no son nombres. Puedes presionar q en cualquier momento para quitar.")

def validator(listaProhibida):
    while True:
        nombre=input("Introduce un nombre o escribe q para quitar: ")
        try:
            nombre=int(nombre)
        except:
            pass
        else:
            print("Eso es un numero! Los numeros no son validos")
            continue
        if nombre=="q":
            break
        else:
            if nombre not in listaProhibida:
                print("El nombre: "+ nombre+ ". Es Valido")
            else:
                print("Nombre prohibido!")

def generador_lista(file):
    archivo=open(file,"r")
    listaProhibida=[nombre.strip() for nombre in archivo]
    return listaProhibida

if __name__=="__main__":
    instrucciones()
    while True:
        invalidNames=["covid", "peo", "nalga", "cuarenteno"]
        opc=int(input("\n1.Generar la lista de nombres prohibidos desde el archivo de text\n2.Trabajar con la lista de nombres prohibidos del programa\n3.Salir\nElija una opcion: "))
        if opc==1:
            validator(invalidNames)
        elif opc==2:
            invalidNames=generador_lista("lista.txt")
            validator(invalidNames)
        elif opc==3:
            break
        else:
            print("\nValor Invalido")
   


