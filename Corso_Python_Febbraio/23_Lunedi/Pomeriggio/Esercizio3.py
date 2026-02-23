'''1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente
numeri interi casuali compresi tra 1 e 100.
2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
3. Inverti le righe della matrice estratta (cioè la prima riga diventa l'ultima, la seconda diventa la penultima, ecc).
4. Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
6. Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale
e la matrice invertita modificata'''

import numpy as np

# Creazione matrice random 6x6
mat = np.random.randint(1,100,(6,6))
print(mat)

# Matrice centrale 4x4
print(mat[1:5,1:5])

# Matrice con righe invertite
mat_invertita = np.flip(mat, axis=0)
print(mat_invertita)

# Diagonale di matrice invertita
diag_invertita = mat_invertita.diagonal()
print(diag_invertita)

# Matrice con -1 al posto dei multipli di 3
for i in np.ndindex(mat_invertita.shape):
    if mat_invertita[i] % 3 == 0:
        mat_invertita[i] = -1
print(mat_invertita)