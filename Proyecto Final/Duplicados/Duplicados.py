'''
Este programa se encarga de identificar archivos duplicados de acuerdo a su logitud textual
'''
import os
import sys
import stat
import hashlib

def instrucciones():
    print("Este programa solicita el nombre de los archivos con los que deseas trabajar y te ayuda a eliminar los archivos duplicados.")

def dir():
    dir=input("Introduce la ubicacion de el directorio con el que deseas trabajar: ")
    return dir

def archivo(archivo1,archivo2):
    archivo1=open(archivo1,"r")
    for line in archivo1.readlines():
        print(line)


if __name__=="__main__":
    instrucciones()
    os.chdir(dir())

    