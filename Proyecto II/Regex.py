'''
Sistema de validacion de Cedulas. Se tomaran a consideracion los siguientes valores como validos:
E: Extranjero
PE: Panameño Nacido en el extranjero
PI: Panameño Indigena
N: Naturalizado
'''
import re

def instrucciones():
    print("Bienvenido al sistema de Validacion de Cedulas con Regex. Es importante recalcar que el sistema toma como base las reglas de cedulacion del Tribunal electoral. No olvides agregar los guiones. ")

def panameno():
    while True:
        cedula=input("\nIngrese su cedula para evaluar su validez, presiona q para terminar: ")
        if cedula.lower()=="q":
            break
        #Hay 2 formas te trabjar con este problema. La mas sencilla es generar 2 regex distintos debido a que la cedulacion es Panama es bastante variante
        else:
            #Este regex revisa los valores en los cuales la primer parte puede ser de 1 caracter
            cedula_1=re.findall(r"\A(N|E)+-\d+-\d",cedula) 

            #Este regex revisa los valores en los cuales la primer parte puede ser de 2 caracteres
            cedula_2=re.findall(r"\A([1-9]|PE|PI)+-\d+-\d",cedula) 

            testLength=cedula.split("-")
            if cedula_1 and len(testLength[0])==1:
                print("\n Excelente! Esta cedula es valida.")
            elif cedula_2 and len(testLength[0])<=2:
                if testLength[0] in "PEPI" or int(testLength[0])<=13: #Revisamos que se mantenga dentro de los estandares de cedulacion de cedula 1 a 13. No más
                    print("\nExcelente! Esta cedula es valida.")
                else:
                    print("\nCedula Invalida")
            else:
                print("\nCedula Invalida")

if __name__=="__main__":
    instrucciones()
    panameno()
    print("\nHasta la proxima")
