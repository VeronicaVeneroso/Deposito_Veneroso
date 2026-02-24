'''Crea uno script Python che esegua i seguenti passaggi:
1. Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a
49. più altre 50 posizioni casuali tra 49 e 101.
 - Stampa l’array, il suo dtype e la sua shape.
2. Modifica il tipo di dato (dtype) dell’array in float64.
 - Verifica e stampa di nuovo dtype e shape.
3. Utilizza lo slicing per ottenere:
 - i primi 10 elementi
 - gli ultimi 7 elementi
 - gli elementi dall’indice 5 all’indice 20 escluso
 - ogni quarto elemento dell'array
4. Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso)
assegnando loro il valore 999.
5. Utilizza la fancy indexing per selezionare:
 - gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
 - tutti gli elementi pari dell’array utilizzando una maschera booleana
 - tutti gli elementi maggiori della media dell'array
6. Stampa:
 - l’array originale dopo tutte le modifiche
 - tutti i sotto-array ottenuti tramite slicing e fancy indexin
'''

import numpy as np

arr = np.concatenate((np.arange(50),np.random.randint(49,101,50)))
print("\nL'array generato è:\n", arr, "\nL'array è di tipo: ", arr.dtype, "\nHa forma: ", arr.shape)

arr_modificato = np.array(arr, dtype='float64')
print("\nL'array con tipo modificato è:\n", arr_modificato, "\nIl nuovo tipo è: ", arr_modificato.dtype, "\nLa nuova forma è: ", arr_modificato.shape)

print("\nI primi 10 elementi dell'array sono:\n", arr[:10])
print("\nGli ultimi 7 elementi dell'array sono:\n", arr[-7:])
print("\nGli elementi dell'array dall'indice 5 al 20 sono:\n", arr[5:20])
print("\nOgni quarto elemento dell'array:\n", arr[::4])

arr2 = arr.copy()
arr2[10:15] = 999
print("\nArray con sostituzione di 999:\n", arr2)

indexing = [0, 3, 7, 12, 25, 33, 48]
arr3 = arr[indexing]
print("\nElementi specifici dell'array:\n", arr3)

print("\nI numeri pari dell'array sono:\n", arr[arr % 2 == 0])

media = np.mean(arr)
print("\nIl valore medio dell'array è: ", media, "\nI valori maggiori della media sono:\n", arr[arr > media])