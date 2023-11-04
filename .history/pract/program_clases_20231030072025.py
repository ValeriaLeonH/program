import random
import numpy as np
from colorama import *

def main():
    def Validar(a):
        if(a<100000000000)or(a>999999999999):
            return False
        else:
            return True

    def Numero(b,c):
        return (b // c)

    def Resto(d,e):
        return (d % e)

    def Distintos(i,j,k):
        if(i==j)or(i==k)or(j==k):
            return False
        else:
            return True
        
    def Promediogeneral(a,b,c,d,e,f):
        return((a+b+c+d+e+f)/6)
    
    def Validar(v):
        if(v>=10 and v<=15):
            print("El numero", v , "esta en 10-15")
        elif(v>=16 and v<=18):
            print("El numero", v ," esta en 16-18")
        elif(v>=19 and v<=20):
            print("El numero", v ," esta en 19-20")
            
    def Prom(t):
        if(t>=10 and t<=15):
            global cont10, sum10
            cont10 = 0 + 1
            sum10 = 0 + t
        elif(t>=16 and t<=18):
            global cont16, sum16
            cont16 = 0 + 1
            sum16 = 0 + t
        elif(t>=19 and t<=20):
            global cont19, sum19
            cont19 = 0 +  1
            sum19 = 0 + t
            
    n=int(input("Indique nÃºmero de 12 dÃ­gitos: "))
    re=Validar(n)    

    if(re==False):
        print("ERROR el numero suministrado es: ",n)
        print("y debe ser un nÃºmero de 12 dÃ­gitos")
    else:
        t1=Numero(n, 10000000000)
        r=Resto(n,10000000000)
        t2=Numero(r, 100000000)
        r=Resto(n, 100000000)
        t3=Numero(r, 1000000)
        r=Resto(n, 1000000)
        t4=Numero(r, 10000)
        r=Resto(n, 10000)
        t5=Numero(r, 100)
        r=Resto(n, 100)
        t6=Numero(r, 1)
        r=Resto(n, 1)

        print("El nÃºmero N es: ",n)
        print("El primer nota es: ",t1)
        print("la segunda nota es: ",t2)
        print("la tercera nota es: ",t3)
        print("la cuarta nota es: ",t4)
        print("la quinta nota es: ",t5)
        print("la sexta nota es: ",t6)

        promedio_general=Promediogeneral(t1, t2, t3, t4, t5, t6)
        print("El promedio general es de : ", promedio_general)    
        
        
        Validar(t1)
        Validar(t2)
        Validar(t3)
        Validar(t4)
        Validar(t5)
        Validar(t6)
        
        Prom(t1)
        Prom(t2)
        Prom(t3)
        Prom(t4)
        Prom(t5)
        Prom(t6)

        print(sum10/cont10)
        print(sum16/cont16)
        print(sum19/cont19)  
main()