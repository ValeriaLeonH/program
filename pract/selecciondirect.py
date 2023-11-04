def ord_seleccion(arreglo):
    for i in range(len(arreglo) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo

        for j in range(i + 1, len(arreglo)): # <-- bucle hijo
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

a = [22, 25, 12, 64, 11]
ord_seleccion(a)

print(a)