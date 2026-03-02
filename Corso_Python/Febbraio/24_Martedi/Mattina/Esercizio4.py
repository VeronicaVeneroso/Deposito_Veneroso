import numpy as np

'''Esercizio 1:
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.'''

print("\n======= Esercizio 1 =======")

arr = np.random.randint(1,100,15)
print("\nL'array generato casualmente è:\n", arr)
sum = np.sum(arr)
print("\nLa somma degli elementi dell'array è: ", sum)
media = np.mean(arr)
print("\nLa media degli elementi dell'array è: ", media)


'''Esercizio 2:
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.'''

print("\n======= Esercizio 2 =======")

mat = np.arange(1,26).reshape(5,5)
print("\nMatrice contenente i numeri da 1 a 25:\n", mat)

col2 = mat[:,1]
print("\nSeconda colonna della matrice:\n", col2)

riga3 = mat[2,:]
print("\nTerza riga della matrice:\n", riga3)

diag = np.diag(mat)
print("\nGli elementi della diagonale sono:\n", diag)
sum_diag = np.sum(diag)
print("\nLa somma degli elementi della diagonale è: ", sum_diag)