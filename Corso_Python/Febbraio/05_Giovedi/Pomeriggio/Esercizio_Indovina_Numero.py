# Scrivi un programma che genera un numero casuale
# tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
# stato generato. Dopo ogni tentativo, il programma dovrebbe
# dire all'utente se il numero da indovinare è più alto o più
# basso rispetto al numero inserito. Il gioco termina quando
# l'utente indovina il numero o decide di uscire.

# Funzione che ci restituisce True se la risposta è giusta, False se è sbagliata
def indovina_numero(prova:int,num_generato:int):
    if prova == num_generato:
        print("Hai indovinato, bravo!")
        risposta = True
    elif prova > num_generato:
        print("Il numero che hai scelto è maggiore di quello giusto")
        risposta = False
    else:
        print("Il numero che hai scelto è minore di quello giusto")
        risposta = False
    return(risposta)



import random
# Genera il numero casuale
x = random.randint(1,100)
print(x)
risposta = False
scelta = "si"
# Ciclo che permette di riprovare ad indovinare se l'utente vuole
while risposta == False and scelta == "si":
    print("Prova ad indovinare il numero che è stato generato:")
    numero = int(input())
    risposta = indovina_numero(numero,x)
    if risposta == False:
        scelta = input("Sbagliato! Vuoi riprovare (si/no)").lower()
