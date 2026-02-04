# Chiedi all'utente di inserire un numero. Il programma
# dovrebbe quindi fare un conto alla rovescia a partire da
# quel numero fino a zero, stampando ogni numero e chiederti
# se vuoi ripetere o no.

risposta = "si"

while risposta.lower() == "si":

    num = int(input("Inserisci il numero da cui vuoi far partire il conto alla rovescia: "))

    for i in range(num, -1, -1):
        print(i)

    risposta = input("Vuoi ripetere il conto alla rovescia? ")

print("Ciclo terminato.")


# Chiedi all'utente di inserire un numero.
# Il programma dovrebbe controllare se il numero inserito è
# pari o no. Se è pari, lo salva e stampa "Il numero
# è pari". Altrimenti, stampa "Il numero è dispari".
# si ferma il tutto quando ha 5 numeri pari

numeri_pari = []

while len(numeri_pari)<5:

    numero = int(input("Inserisci un numero: "))
    z = numero % 2

    if z == 0:
        numeri_pari.append(numero)
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

print(numeri_pari)