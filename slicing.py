import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

arr = np.array(lista)
print(type(arr))  

matriz = ([[1,2,3],[4,5,6],[7,8,9]]) # matriz 3x3
matriz = np.array(matriz) # damos formato de arrai
print(matriz) # imprimimos la matriz

arr[1] = 0 # cambiamos el valor de la posicion 1
print(arr[1])
print("________")

print(matriz[0])
print(matriz[2])
print("________")
print(matriz[0,2])
print("________")
print(arr[2:9])
print(matriz[1,2:9])
