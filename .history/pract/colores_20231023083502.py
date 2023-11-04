#Librerias a Importar
import numpy as np  #LibrerÃ­a NumÃ©rica y de Arreglos
import os     #LibrerÃ­a de comandos del Sistema Operativo
import time   #LibrerÃ­a para manejar el tiempo 
from colorama import *   #LibrerÃ­a para manejar col?ores del texto,fondo y estilo
#from colorama import init, Fore, Back, Style

def main():
    init(autoreset=True) #Sirve para quitar el color
    #Encabezado
    print(Fore.BLUE+"UCAB Elaborado por: ".center(60," "))        
    print()
    #Datos de Entrada
    print(Fore.RED+"Indique NÂº entero positivo de 6 dÃ­gitos ",end=' ')
    n=int(input())
    #Borrar Pantalla
    os.system("cls")
    #Procesamiento de Datos
    pd=(n // 100000)
    r=(n % 100000)
    n1=(r // 100)
    up=(r % 100)
    n2=((pd*100)+up)
    if(n1>=n2):
        may=n1
    else:
        may=n2   

    #Salida de Datos    
    print(Fore.RED+"UCAB Elaborado por: ".center(60," "))    
    print()
    print(Fore.BLUE+"El nÃºmero N es: ",n)
    print(Fore.BLUE+"El nÃºmero N1 es: ",n1)
    print(Fore.BLUE+"El nÃºmero N2 es: ",n2)
    print(Fore.BLUE+"El Mayor entre N1 y N2 es: ",may)

main()