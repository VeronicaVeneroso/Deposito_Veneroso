'''Crea un array NumPy utilizzando arange e verifica il tipo
di dato (dtype) e la forma (shape) dell'array

Esercizio:
1. Utilizza la funzione np.arange per creare un array di numeri
interi da 10 a 49.
2. Verifica il tipo di dato dell'array e stampa il risultato.
3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo
il tipo di dato.
4. Stampa la forma dell'array'''

import numpy as np

arr = np.arange(10,50)
print("L'array generato è: ", arr)
print("Il tipo di dato è: ", arr.dtype)
type = arr.astype(np.float64)
print("Il nuovo array è: ", type)
print("Il nuovo tipo di dato è: ", type.dtype)
print("La forma dell'array è: ", arr.shape)

array = np.linspace(5,10,10)
print(array)
reshaped_array = array.reshape((2,5))
print(reshaped_array)

