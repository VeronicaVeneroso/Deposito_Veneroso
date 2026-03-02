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

# Chiede all'utente di inserire un numero intero positivo finché il valore inserito è corretto
n = 0
while n <= 0:
        n = int(input("Inserisci un numero intero positivo: "))
        if n <= 0:
            print("Il numero inserito non è corretto.")
print("Numero inserito correttamente: ", n)


# Genera e stampa una lista di lunghezza n di numeri compresi tra 1 e n
import random
lista = []
for i in range(n):
    lista.append(random.randint(1,n))
print("La lista di numeri generati casualmente è: ", lista)


# Calcola la somma dei numeri pari e la somma di tutti i numeri presenti nella lista
# e crea la lista contenente i numeri dispari della lista
somma_pari = 0
totale = 0
dispari = []
for i in lista:
    totale = totale + i
    if i % 2 == 0:
        somma_pari = somma_pari + i
    else:
        dispari.append(i)
dispari = set(dispari)
print("La somma dei numeri pari presenti nella lista è: ", somma_pari)
print("I numeri dispari presenti nella lista sono: ", dispari)

# Controlla e stampa se la somma di tutti i numeri della lista è primo oppure no
if totale < 2:
    primo = False
else:
    primo = True
    for i in range(2, totale):
        if totale % i == 0:
            primo = False
            break
if primo:
     print("La somma di tutti i numeri nella lista è un numero primo: ", totale)
else:
    print("La somma di tutti i numeri nella lista non è un numero primo: ", totale)


insieme = set(lista)
numeri_primi = []
for numero in insieme:
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
