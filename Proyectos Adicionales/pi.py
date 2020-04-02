'''

Este programa acepta un valor que nos permitira redondear pi hasta ese valor decimal. 
Por ejemplo si intrucimos el numero 4: recibimos 3.1415.
Si introducimos el numero 2: recibimos 3.14

'''
import math #importar el modulo Math

def pi_round(value): #Funcion que redondea Pi
    if value>15:
        return f"Bueno, tecnicamente pi no llega taaaan lejos. El valor de pi completo es: {math.pi}"
    else:
        return f"El valor redondeado de pi es {round(math.pi,value)}"


if __name__=="__main__":
    while True: #Revisar que el valor sea un numero
        try:
            value=int(input("Ingrese hasta que valor quiere redondear pi: "))
        except:
            print("Whoops! Hubo un error. Intente Nuevamente")
        else:
            break
    
    print(pi_round(value))





