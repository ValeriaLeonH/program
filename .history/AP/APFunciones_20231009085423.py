#Dado un numero de 9 dÃ­gitos validar 
#esta condicion y en caso de cumplirla
#formar tres trios T1=3 primeros 
#nÃºmeros, T2=tres siguientes y
#T3=tres Ãºltimos, y luego si los
# tres trios son distintos Sumarlos
# y mostrar el resultado. 
def main():
    # Definicion de las Funciones
    
    def Validar(a):
        if(a<100000000)or(a>999999999):
            return False
        else:
            return True
    
    def Numero(b,c):
        return (b // c)

    def Resto(d,e):
        return (d % e)

    def Sumar(f,g,h):
        return (f+g+h)

    def Distintos(i,j,k):
        if(i==j)or(i==k)or(j==k):
            return False
        else:
            return True

    # Inicio Programa Principal
    print("UCAB Elaborado por: ")
    print()
    n=int(input("Indique nÃºmero de 9 dÃ­gitos: "))
    re=Validar(n)
    if(re==False):
        print("ERROR el numero suministrado es: ",n)
        print("y debe ser un nÃºmero de 9 dÃ­gitos")
    else:
        t1=Numero(n,1000000)
        r=Resto(n,1000000)
        t2=Numero(r,1000)
        t3=Resto(r,1000)
        if(Distintos(t1,t2,t3)==False):
            print("El nÃºmero N es: ",n)
            print("El primer trio es: ",t1)
            print("El segundo trio es: ",t2)
            print("El tercer trio es: ",t3)
            print("y por no ser todos distintos")
            print("NO se pueden sumar")
        else:
            res=Sumar(t1,t2,t3)
            print("El nÃºmero N es: ",n)
            print("El primer trio es: ",t1)
            print("El segundo trio es: ",t2)
            print("El tercer trio es: ",t3)
            print("El resultado de la Suma es: ",res)
               
main()