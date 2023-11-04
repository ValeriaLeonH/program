""".- Mostrar y sumar todos los DIVISORES de un número N entero positivo mayor
que cero dado por el usuario.
 .- Mostrar los números de N a cero (0), donde N es un número entero positivo de
dos dígitos y se desea además, contar la cantidad de números Impares que hay en este
conjunto de números.
 .- Mostrar los 5 primeros números menores que 50 que sean divisibles por un
número entero positivo N dado.
  Salir del Algoritmo"""
  
import numpy as np
from colorama import *

def main():
  print(" 1-Mostrar y sumar todos los DIVISORES de un número N entero positivo mayor")
  print("2. Mostrar los números de N a cero (0) de 2 digitos")
  print("3. Mostrar los 5 primeros números menores que 50 que sean divisibles por un número entero positivo")
  print("4.Salir")
  
  n=int(input("Que operacion desea realizar "))
  if n==1:
    cont=0
    contb=0
    num=int(input("Ingrese un numero a operar "))
    for divisor in range(1,num+1):
      if(num % divisor) == 0:
        print(divisor, "es divisor de ", num)
        cont += 1
        contb += +divisor
    print("el numero ", num ," tiene ",cont," divisores y la suma de sus divisores es", contb)
    
  elif n==2:
    num=int(input("Ingrese un numero a operar"))
    if(num>=10 and num<=99):
      for i in range(1, num+1):
        print(num-i)
    else:
      print("El numero debe tener dos digitos")
        
  elif n==3:
    cont = 0
    num=int(input("Ingrese un numero a operar"))
    for divisor in range (1, num+1):
      if (num % divisor) == 0:
        cont += 1
        while(cont<6):
          print(divisor, "es divisor de ", num)
          break
          
  elif n==4:
    end=''
    
  else: 
    print("Esa opcion no esta disponible, vuelva a intentar")
main()
