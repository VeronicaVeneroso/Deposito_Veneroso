'''Consegna:
1. Crea un array NumPy 10 di 20 numeri interi casuali compresi tra 10 e 50.
2. Utilizza lo slicing per estrarre i primi 10 elementi.
3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.'''

import numpy as np

arr = np.random.randint(10,50,20)
print(arr)
print(arr[:-10])
print(arr[-5:])
print(arr[5:15])
print(arr[::3])
arr[5:10] = 99
print(arr)