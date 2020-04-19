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

def panameno(cedula):
            cedula_1=re.findall(r"\A(N|E)+-\d+-\d",cedula) 
            #Este regex revisa los valores en los cuales la primer parte puede ser de 2 caracteres
            cedula_2=re.findall(r"\A([1-9]|PE|PI)+-\d+-\d",cedula) 
            testLength=cedula.split("-")
            if cedula_1 and len(testLength[0])==1:
                return "\nExcelente! Esta cedula es valida."
            elif cedula_2 and len(testLength[0])<=2:
                if testLength[0] in "PEPI" or int(testLength[0])<=13: #Revisamos que se mantenga dentro de los estandares de cedulacion de cedula 1 a 13. No más
                    return "\nExcelente! Esta cedula es valida."
                else:
                    return "\nCedula Invalida"
            else:
                return "\nCedula Invalida"

if __name__=="__main__":
    instrucciones()
    while True:
        cedula=input("\nIngrese su cedula para evaluar su validez, presiona q para terminar: ")
        if cedula.lower()=="q":
            break
        else:
            print(panameno(cedula))
    print("\nHasta la proxima")
