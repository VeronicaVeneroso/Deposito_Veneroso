# Punto 1: Utilizzo di if
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
# e "Dispari" se il numero è dispari.

# numero inserito dall'utente
num = int(input("Inserisci un numero: "))

# controlla se il numero è pari o dispari con il modulo
if num % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")


# Utilizzo di while e range
# Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
# numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripetere all’infinito

# numero inserito dall'utente
numero = int(input("Inserisci un numero intero positivo: "))
# inizializzazione variabile risposta
risposta = "si"

# finché la risposta è sì continua a ripetere il conto alla rovescia
while risposta.lower() == "si":
    for i in range(numero, -1, -1):
        print(i)
    risposta = input("Vuoi ripetere il conto alla rovescia? ")
print("Ciclo terminato.")


# Utilizzo di for
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
# ciascun numero nella lista.

# inizializzazione della lista
lista = []
# chiede all'utente se vuole riempire la lista
risposta = input("Vuoi inserire elementi nella lista? (si/no) ")

# finché l'utente vuole aggiungere numeri alla lista continua ad allungarla
while risposta.lower() == "si":
    nr = int(input("Inserisci un numero intero: "))
    lista.append(nr)
    risposta = input("Vuoi aggiungere ancora numeri alla lista? (si/no) ")

# stampa i quadrati di tutti gli elementi della lista
for i in lista:
    print(i**2)


# Utilizzo di if, while e for insieme. Scrivi un sistema che prende in input
# una lista di numeri interi che precedentemente è stata valorizzata dall’utente.
# Il sistema deve:
# 1.Utilizzare un ciclo for per trovare il numero massimo nella lista.
# 2.Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
# 3.Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
# altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

# controlla se la lista è vuota
if len(lista) == 0:
    print("La lista è vuota")
# se la lista non è vuota calcola il max con un confronto uno a uno
else:
    max = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > max:
            max = lista [i]
    lunghezza = 0
    
    # conta il numero di elementti nella lista
    while lunghezza < len(lista):
        lunghezza = lunghezza + 1

    print("Il massimo della lista è: ", max)
    print("Il numero di elementi presenti nella lista è:", lunghezza)
