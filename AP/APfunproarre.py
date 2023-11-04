import random
import numpy as np

def main():
    #Variables Globales
    sp=int
    v1=np.array([1,2,3,4])
    v2=np.array([0]*4)
    v3=np.array([0]*4)

    #Funciones y Procedimientos
    def Sumar(a,b):
        s=(a+b)
        return s

    def Multi(c,d):
        global m
        m=(c*d)

    def Sump():
        #nonlocal v1
        nonlocal sp        
        sp=0        
        for i in range(0,4,1):
            if ((v1[i] % 2)== 0):
                sp=(sp+v1[i])
        print("El valor de SP en la funcion: ",sp) 

    def Llenv2():
        for j in range(0,4,1):
            v2[j]=random.randint(1,4)

    def Priult(v1,v2):
        j=3
        for i in range(0,4,1):
            if(v1[i]>v2[j]):
                v3[i]=v1[i]
            else:
                v3[i]=v2[j]
            j -=1 
    
        
    #Programa Principal
    #Entrada de Datos
    x=int(input("indique numero entero X: "))
    y=int(input("indique numero entero y: "))
        
    #Procesamiento de Datos
    sum=Sumar(x,y)
    Multi(x,y)
    Sump()
    Llenv2()
    Priult(v1,v2)

    #Salida de Datos
    print("El valor de X es: ",x)
    print("El valor de y es: ",y)
    print("La Suma de X mas Y es: ",sum)
    print("El Producto de X por Y es: ",m)
    print("El arreglo V1 es: ")
    print(v1)
    #print("La suma de numeros Pares de V1 es: ",sp)
    print("El arreglo V2 es: ")
    print(v2)
    #print("El arreglo V3 es: ")
    #print(v3)
main()    