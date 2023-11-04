""" ciclo
1 Solicitar numero de 4 digitos
2 Separar digitos
3 Sumar numeros n1 y n2 (n1, n2)
4 par (sum)
5 Determinar ganador
cont1=(cont1+1)
cont2 =(cont2+1) 
Todo debe ir en ciclo de 3 juegos 
Fuera debe indicar el ganador"""

import random
import numpy as np

def main():
    cont1 = 0 
    cont2 = 0
    
    def Separar(n):
        j1=(n // 1000)
        r=(n % 1000) ## resto
        n1=(r // 100)
        r=(r % 100)
        j2=(r // 10)
        n2=(r % 10)
    
    def Sum(n1, n2):
        sumar = n1+n2
        return sumar
    
    def Par(sum):
        par = ((sum % 2)==0)
        
    while(cont1<3) or (cont2<3):
        n=int(input("Ingrese un numero de 4 digitos"))
        Separar(n)
        sum = Sum(n1, n2)
        if (Par(sum)==True):
            if(j1==1):
                cont1=cont1+1
            else:
                cont2= cont2+1
        else: 
            if (j1==2):
                cont1= cont1+1
            else:
                cont2 = cont2+1
                
        if (cont1<3) or (cont2<3):
            print("Gana el jugador 1")
        else: 
            print("Gana el jugador 2")
main()
