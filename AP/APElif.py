def main():
    t=int(input("Indique su Turno (1, 2 o 3): "))
    if(t==1):
        r="MaÃ±ana"
    elif(t==2):
        r="Tarde"
    elif(t==3):
        r="Noche"
    else:
        r="ERROR en Turno debe ser un valor del 1 - 3"
    print("Su turno en nÃºmero es: ",t)    
    print("y corresponde al turno de la: ",r)

   
main()