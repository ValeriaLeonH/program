import random
import numpy as np

def main():
    t=np.array([" "]*5) ##El espacio en blanco es para caracteres
    h=np.array([1,2,3,4,5])
    p=np.array([0]*5)

    def Llent(t):
        for i in range (0, 5, 1):
            x = random.randint(1,3)
            if (x==1):
                t[i]="M"
            elif(x==2):
                t[i]="T"
            else:
                t[i]="N"
    

    # Entrada de datos
    Llent(t)
    Calc

    #Procesamiento de datos



    #Salida de datos


    print("Elaborado por Valeria Leon")
    print("El arreglo turnos es : ")
    print(t)
    print("El arreglo de horas es : ")
    print(h)
        
        




main()