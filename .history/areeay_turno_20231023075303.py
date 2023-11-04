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
    
    def Calcp(p):
        for i in range (0,5,1):
            if(t[i]=="M"):
                p[i] = (h[i]*10) ## t[i] el arreglo que evaluamos, p[i] donde guardamos el pago y h[i] es la hora * la cantidad de dolares por hora
            elif(t[i]=="T"):
                p[i]=(h[i]*20)
            else: 
                p[i]=(h[i]*30)

    def Sump(p):
        s=0
        for i in range (0,5,1):
            s = (s + p[i]) ## s es local, porque la uso dentro
        return s

    def Promp(p):
        p = (sum//5)
        
    # Entrada de datos
    Llent(t)
    Calcp(p) #el arreglo que quiero calcular
    sum = Sump(p) ##Le pasamos p porque queremos sumar los elementos del arreglo p
    prom = Promp(p)

    #Procesamiento de datos



    #Salida de datos


    print("Elaborado por Valeria Leon")
    print("El arreglo turnos es : ")
    print(t)
    print("El arreglo de horas es : ")
    print(h)
    print("El arreglo de pagos diarios es : ")
    print(p)
    print("La suma de todos los pagos es de : ", sum)

main()