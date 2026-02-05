''' Scrivi un programma che esegua le seguenti operazioni:
1.Chiedi all'utente di inserire un numero intero positivo n. Se l'utente
inserisce un numero negativo o zero, continua a chiedere un numero fino a
quando non viene inserito un numero positivo.
2.Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza
della lista deve essere n.
3.Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella
lista.
4.Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
5.Utilizza una funzione per determinare se un numero è primo. La funzione deve
restituire True se il numero è primo, altrimenti False.
6.Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
7.Infine, utilizza una struttura if per determinare se la somma di tutti i
numeri nella lista è un numero primo e stampa il risultato '''
# EXTRA: Creare inizialmente le collezioni come tuple e trasformarle in liste solo all'esigenza

# Punto 1:

n = 0
# Chiede all'utente di inserire un numero intero positivo finché il valore inserito è corretto
while n <= 0:
        n = int(input("Inserisci un numero intero positivo: "))
        if n <= 0:
            print("Il numero inserito non è corretto.")
print("Numero inserito correttamente: ", n)


# Punto 2:

import random
# Genera e stampa una tupla di lunghezza n di numeri compresi tra 1 e n
elenco = tuple(random.randint(1,n) for _ in range(n))
print("L'elenco di numeri generati casualmente è: ", elenco)


# Punto 3:

somma = 0
# Calcola la somma dei numeri pari presenti nella lista
for i in elenco:
    if i % 2 == 0:
        somma = somma + i
print("La somma dei numeri pari presenti nella lista è: ", somma)


# Punto 4:

# Crea una tupla contenente i numeri dispari dell'elenco e la stampa
dispari = tuple(i for i in elenco if i % 2 != 0)
print("I numeri dispari presenti nella lista sono: ", dispari)

'''
# Punti 5/6/7:

numeri_primi = []
totale = 0
for numero in lista:
    # Calcola la somma di tutti i numeri della lista
    totale = totale + numero
    # Valuta se un numero è primo
    if numero < 2:
        primo = False
    else:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

    # Crea una lista di numeri primi e stampa per ogni numero se è primo oppure no
    if primo:
         numeri_primi.append(numero)
         print("Il numero", numero, " è primo")
    else:
         print("Il numero", numero, " non è primo")
print("L'elenco di numeri primi presenti nella lista è: ", numeri_primi)

# Controlla e stampa se la somma di tutti i numeri della lista è primo oppure no
if totale < 2:
    primo = False
else:
    primo = True
    for i in range(2, numero):
        if totale % i == 0:
            primo = False
            break
if primo:
     print("La somma di tutti i numeri nella lista è un numero primo: ", totale)
else:
    print("La somma di tutti i numeri nella lista non è un numero primo: ", totale)'''