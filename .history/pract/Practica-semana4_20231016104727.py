import random
import numpy as np

def main():
    #Variables Globales
    v1=np.array([0]*4)
    v2=np.array([0]*4)
    v3=np.array([0]*4)

    #Funciones y Procedimientos

    def Sump(v1,v2):    
        for i in range(0,4,1):
            v3[i]=(v1[i]+v2[i])//2
        

    def Llenv1(n):
        for j in range(0,4,1):
            n[j]=random.randint(10,20)

    def Mayor(n):
        mayor = n[0]
        for i in range(1,4,1):
           if (mayor<n[i]):
               mayor = n[i]
        return (mayor)
        
    #Procesamiento de Datos
    Llenv1(v1)
    Llenv1(v2)
    Sump(v1,v2)

    #Salida de Datos
    print("El arreglo V1 es: ")
    print(v1)
    print("El arreglo V2 es: ")
    print(v2)
    print("El promedio de los dos vectores es")
    print(v3)
    mayor = Mayor(v3)
    print("La mayor nota es: ", mayor)
main()    