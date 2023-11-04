#Librerias a Importar
import random
import numpy as np
from colorama import *
def main():
init(autoreset=True)
#a=np.array([6,3,2,4,9,7])
a=np.array([0]*6) # inicializa un Arreglo de 6 posiciones con cero (0)

for i in range(0,6,1):
a[ i ] =random.randint(1,10) # genera números aleatorios enteros del 1 al 10