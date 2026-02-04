# lista di numeri
numeri = [1, 2, 3, 4, 5]
# lista di stringhe
nomi = ["Alice", "Bob", "Charlie"]
# lista di tipi misti
misto = [1, "due", True, 4.5]

# gli indici di una collezione vanno da 0 a lunghezza_della_lista-1
print(numeri[0]) # stampa il primo elemento della lista numeri
print(numeri[2]) # stampa il terzo elemento della lista numeri

# lista di liste (tabella/database)
ldl = [numeri, nomi, misto]
print(ldl)

# modifica elemento della lista
numeri[2] = 10
print(numeri)

#print(numeri[7]) # errore IndexError

print(len(numeri)) # stampa la lunghezza della lista
numeri.remove(1) # rimuove il valore 1 dalla lista
print(numeri)
numeri.append(100) # aggiunge in ultima posizione il valore 100
print(numeri)
numeri.insert(2,20) # inserisce il valore 20 in posizione 2 (cioè terza posizione)
print(numeri)
numeri.sort() # ordina la lista in senso crescente
print(numeri)

# esempi di Tupla (costante, non modificabile)
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

print(punto[0])
print(punto[1])

# punto[0] = 5 # Non si può modificare una Tupla
# punto.append(2) # Non si può aggiungere nulla a una Tupla


punto2 = 3, 4 # Tuple packing (Crea Tupla (3,4))
x, y = punto2 # Tuple unpacking (Chiama x il primo elemento della tupla e y il secondo)
print(x, y)
print(punto2)

tupla = 2,3,4
lista2 = list(tupla) # Trasforma la tupla in lista
print(tupla)
print(lista2)

# esempi di insiemi
set1 = set([1, 2, 3, 4, 5]) # Trasforma una lista in un insieme
print(set1)
set2 = {4, 5, 6, 7, 8}
print(set2)
set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3)

# Operazioni algebriche sugli insiemi
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Unione
print(set1.intersection(set2)) # Intersezione
print(set1.difference(set2)) # Differenza
print(set1.symmetric_difference(set2)) # Differenza simmetrica