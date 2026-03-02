import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr2d = np.array([[1,2,3],[4,5,6]])

print("Forma dell'array:", arr.shape)
print("Dimensioni dell'array:",arr.ndim)
print("Tipo di dati:", arr.dtype)
print("Numero di elementi:", arr.size)
print("Somma degli elementi:", arr.sum())
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax())

array = np.arange(6)
print(array)

reshaped_arr = array.reshape((2,3))
print(reshaped_arr)

arr3 = np.array([1,2,3,4,5])
print(arr[0])

# Slicing
print(arr[1:3])

# Boolean Indexing
print(arr[arr > 2])

arr4 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

# Slicing sulle righe
print(arr4[1:3])

# Slicing sulle colonne
print(arr4[:, 1:3])

# Slicing misto
print(arr4[1:3, 1:3])

arr5 = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr5[2:7])
print(arr5[1:8:2])
print(arr5[:5])
print(arr5[5:])

print(arr5[-5:])
print(arr5[:-5])

# Fancy Indexing
arr6 = np.array([10,20,30,40,50])
indices = np.array([1,3])
print(arr6[indices])

indices2 = [0,2,4]
print(arr6[indices2])