'''1. Chieda all’utente di inserire un numero intero positivo. 
2. Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
3. Per ogni numero:
-stampi "pari" se il numero è pari 
-stampi "dispari" se il numero è dispari 
4. Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.'''
# Inizializzazione variabili
numero = 0
risposta = "si"
# Ciclo per ripetere le operazioni tutte le volte che è necessario
while numero <= 0 and risposta == "si":
    # Inserimento numero in input
    print("Inserisci un numero intero positivo:")
    numero = int(input())
    # Controlla se il numero inserito è positivo oppure no
    if numero <= 0:
        print("Il numero inserito non è corretto! Riprova!")
    else:
        # Stampa tutti i numeri fino a quello inserito indicando per ognuno se è pari o dispari
        for i in range(1,numero + 1, 1):
            if i % 2 == 0:
                print(i, "pari")
            else:
                print(i, "dispari")
        # Inizializza nuovamente la variabile numero per il caso in cui si voglia ripetere il ciclo
        numero = 0
        # Richiede all'utente se vuole ripetere il procedimento
        risposta = input("Vuoi ripetere il procedimento? (si/no)").lower()
