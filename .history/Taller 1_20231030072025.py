import numpy as np
import random
from colorama import *

def main():
  init(autoreset=True)
  CS1 = np.array(["X","X","X","X","X","X","X","X","X","X"])
  CS2 = np.array([" "]*10)
  S = np.array(["       "]*10)
  h=0
  m=0
  promh= 0
  prom = 0
  porch = 0
  porcm = 0


  def LlenCS2(CS2):
    for i in range (0,10,1):
      x = random.randint(1,2)
      if (x==1):
        CS2[i]="X"
      else: 
        CS2[i]="Y"

  def Calc(S):
    for i in range (0,10,1):
      if (CS1[i]==CS2[i]):
        S[i] = "Mujer"
      else:
        S[i] = "Hombre"

  def Suma(s):
    nonlocal h,m
    for i in range (0,10,1):
      if (s[i]=="Mujer"):
        m = m + 1
      else: 
        h = h + 1

  def Promedio(x):
    return (x / 10)

  def Porcentaje(x):
    return (x * 100)



  LlenCS2(CS2)
  Calc(S)
  Suma(S)
  prom = Promedio(m)
  promh = Promedio(h)
  porcm = Porcentaje(prom)
  porch = Porcentaje(promh)

  print()
  print(Fore.BLUE+"UCAB, Elaborado por RAMÓN MUÑOZ y VALERIA LEON\n".center(100," "))
  print(Fore.GREEN+"El arreglo CS1 FIJO es ")
  print( CS1,"\n")
  print(Fore.GREEN+"El arreglo CS2 aleatorio es ")
  print(CS2,"\n")
  print(Fore.GREEN+"El arreglo resultado de los exos es : ")
  print(S,"\n")
  print(Fore.MAGENTA+"La cantidad de mujeres es ",m, Fore.LIGHTCYAN_EX+" y hombres es ",h,"\n")
  print(Fore.MAGENTA+"El promedio de mujeres es  ", prom, Fore.LIGHTCYAN_EX+" y el promedio de hombre es de ", promh ,"\n")
  print(Fore.MAGENTA+"El porcentaje de mujeres es ", int(porcm),"%", Fore.LIGHTCYAN_EX+" y el porcentaje de hombres es ", int(porch),"%","\n")

main()