# Scrivi un programma che chieda all'utente di inserire un numero
# intero positivo n. Il programma deve poi eseguire le seguenti operazioni:
# 1.Utilizzare un ciclo while per garantire che l'utente inserisca un numero
# positivo. Se l'utente inserisce un numero negativo o zero, il programma deve
# continuare a chiedere un numero fino a quando non viene inserito un numero
# positivo.
# 2.Utilizzare un ciclo for con range per calcolare e stampare la somma dei
# numeri pari da 1 a n.
# 3.Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# 4.Utilizzare una struttura if per determinare se n è un numero primo. Un numero
# primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se
# n è primo o no.


lista = []
risposta = "si"

while risposta == "si":
    n = 0
    # Punto 1:
    while n <= 0:
        n = int(input("Inserisci un numero intero positivo: "))
        lista.append("Numero inserito:")
        lista.append(n)
        if n <= 0:
            print("Il numero inserito non è corretto.")
            lista.append("Numero inserito non corretto")
    print("Numero inserito correttamente")
    lista.append("Numero inserito correttamente")
        
    # Punto 2:
    somma = 0
    for i in range(0,n,2):
        somma = somma + i
    print(somma)
    lista.append("La somma dei numeri pari fino a quello scelto è:")
    lista.append(somma)

    # Punto 3:
    lista.append("Salvo i numeri dispari da 1 al numero scelto")
    for i in range(1,n,2):
        print(i)
        lista.append(i)
    
    # Punto 4:
    if n < 2:
        print("Il numero non è primo")
        list.append("Il numero scelto non è un numero primo")
    else:
        primo = True

        for i in range(2, n):
            if n % i == 0:
                primo = False
                break

        if primo:
            print("Il numero è primo")
            lista.append("Il numero scelto è un numero primo")
        else:
            print("Il numero non è primo")
            lista.append("Il numero scelto non è un numero primo")
    risposta = input("Vuoi ripetere il procedimento? (si/no) ").lower()

print("I tentativi effettuati sono i seguenti: ", lista)


# Creare una lista che salva tutti i tentativi e un'ultima sezione del programma che permetta di visionare o modificare la lista
