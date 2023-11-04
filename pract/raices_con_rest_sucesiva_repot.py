import numpy as np
from colorama import *

def main():
  n=int(input("Ingrese un numero cualquiera "))
  k = n
  cont = 1
  contb = 0
  while(n>0):
    y = n-cont
    x = y-n
    n = n + x
    cont = cont + 2
    contb = contb + 1
  if (k%2 == 0):
    print("La raiz de", k," es ",contb)
  elif (k%3 == 0):
    print("La raiz de", k," es ",contb-1)
main()

