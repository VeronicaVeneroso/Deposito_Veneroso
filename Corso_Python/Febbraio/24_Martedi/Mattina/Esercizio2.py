'''1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
2. Cambia la forma dell'array a una matrice 3x4.
3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
4. Calcola e stampa la somma degli elementi di entrambe le matrici.'''

import numpy as np

arr = np.linspace(0,1,12)
print("\nL'array generato con linspace è:\n", arr)

matr = np.reshape(arr, (3,4))
print("\nLa matrice ricavata dall'array è:\n", matr)

sum_matr = np.sum(matr)
print("La somma degli elementi della matrice è:\n", sum_matr)

mat = np.random.rand(3,4)
print("\nLa matrice generata casualmente è:\n", mat)

sum_mat = np.sum(mat)
print("La somma degli elementi della seconda matrice è:\n", sum_mat)