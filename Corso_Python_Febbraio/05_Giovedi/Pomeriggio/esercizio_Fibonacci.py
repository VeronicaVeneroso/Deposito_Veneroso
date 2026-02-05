# Sequenza di Fibonacci fino a N
# Descrizione: Chiedi all'utente di inserire un numero N. Il
# programma dovrebbe stampare la sequenza di Fibonacci fino a N.
# Ad esempio, se l'utente inserisce 100, il programma dovrebbe
# stampare tutti i numeri della sequenza di Fibonacci minori o
# uguali a 100.

def fibonacci(n:int):
    somma = 0
    serie = [0,1]
    if n > 1:
        somma = 0
        while somma < n:
            somma = serie[-1] + serie[len(serie)-2]
            if somma <= n:
                serie.append(somma)
    return(serie)

numero = 0
risposta = "si"
while numero <= 0 and risposta == "si":
    print("Inserisci un numero intero positivo: ")
    numero = int(input())
    if numero <= 0:
        print("Valore non ammesso. Riprova.")
    else:
        fibo = fibonacci(numero)
        print(fibo)
        risposta = input("Vuoi ripetere il procedimento? (si/no)").lower()
        if risposta == "si":
            numero = 0
