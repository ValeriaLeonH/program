#Librerias a Importar
import random
import numpy as np
from colorama import *

def main():
    init(autoreset=True)
    #a=np.array([6,3,2,4,9,7])
    a=np.array([0]*6)
    for i in range(0,6,1):
        a[i]=random.randint(1,10)
    r=np.array([" ","I","II","III","IV","V","VI","VII","VIII","IX","X"])
    print(Fore.RED+"UCAB  Elaborado por: ")
    print(Fore.BLUE+"Los nÃºmeros del arreglo Arabigo son: ")
    print(a)
    print(Fore.BLUE+"Los nÃºmeros del arreglo Romano son: ")
    for j in range (1,11,1):
        print(r[j],end=' ')
    print()
    print(Fore.BLUE+"Los nÃºmeros Arabigos a Romano son: ")
    for i in range (0,6,1):
        for j in range (1,12,1):
            if (a[i] == j):
                ro=r[j]
                print(Fore.RED+"El nÃºmero Arabigo ",a[i],Fore.RED+" en Romano es: ",ro)
                break
main()
           

