'''

Este programa acepta un valor que nos permitira redondear e hasta ese valor decimal. 
Por ejemplo si intrucimos el numero 4: recibimos 2.7182.
Si introducimos el numero 2: recibimos 2.71

'''
import math #importar el modulo Math

def e_round(value): #Funcion que redondea e
    return f"El valor redondeado de e es {round(math.e,value)}"


if __name__=="__main__":
    while True: #Revisar que el valor sea un numero
        try:
            value=int(input("Ingrese hasta que valor quiere redondear e: "))
        except:
            print("Whoops! Hubo un error. Intente Nuevamente")
        else:
            break
    
    print(e_round(value))

