"""Problema 5: Dado un arreglo de 10 posiciones que almacena números enteros del
0-20 correspondientes a las Notas de los estudiantes de la materia de Algoritmos y
Programación, se desea elaborar un Algoritmo que calcule el Promedio de Notas
General, Promedio de Notas de los estudiantes Aprobados (10 – 20), promedio de
Notas de los estudiantes Reprobados, y además incremente un punto adicional,
otorgado por el profesor, SOLO a aquellos estudiantes reprobados con una Nota
Mayor a 7 puntos."""

import numpy as np

def main():
  v=np.array([0]*10)
  
  def Validar(v):
    if (v>=0 and v<=20):
      return True
    else: 
      return False
      
  for i in range(1,11,1):
    cont = 0
    suma = 0
    print("Ingrese la nota numero ", i)
    num=int(input( ))
    re = Validar(num)   
    
    if(re==False):
        print("ERROR el numero suministrado es: ", num)
        print("y debe ser un numero de 2 digitos, vuelva a intentar")
        end=''
    else:
      if(num>=10 and num <=20):
        suma += num
        cont += 1
  print("El promedio de notas es de ", suma/cont)
  
main()