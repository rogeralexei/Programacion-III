'''
Este programa permite al usuario validar un nombre o una lista de nombres
'''
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
        if nombre.lower()=="q":
            break
        else:
            if nombre.lower() not in listaProhibida:
                print("El nombre: "+ nombre+ ". Es Valido")
            else:
                print("Nombre prohibido!")


if __name__=="__main__":
   #La lista de abajo es una lista que se utilizo para hacer pruebas, quitar el comentario para trabajar con ella.
   invalidNames=["covid", "peo", "nalga", "cuarenteno"]
   instrucciones()
   validator(invalidNames)
   


