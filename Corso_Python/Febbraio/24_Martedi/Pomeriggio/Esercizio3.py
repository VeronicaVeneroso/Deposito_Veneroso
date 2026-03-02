'''Creare un array NumPy di forma (4,4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1),
(1,3), (2,2) e (3,0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando
la numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.'''

import numpy as np

mat = np.random.randint(10,50,16).reshape(4,4)
print("\nLa matrice 4x4 generata casualmente è:\n", mat)

index_row = [0, 1, 2, 3]
index_col = [1, 3, 2, 0]
print("\nGli elementi corrispondenti agli indici specifici selezionati sono:\n", mat[index_row, index_col])

righe_disp = np.arange(mat.shape[0])[1::2]
print("\nLe righe dispari della matrice sono:\n", mat[righe_disp,:])

new_mat = mat + 10
print("\nMatrice iniziale con incremento di 10 su ogni elemento:\n", new_mat)