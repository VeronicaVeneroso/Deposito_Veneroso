'''1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2. Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3. Somma i due array elemento per elemento per ottenere un nuovo array.
4. Calcola la somma totale degli elementi del nuovo array.
5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6. Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
7. Salva i dati su un file TXT a ogni giro.
8. Rendi ripetibile il processo complessivo.
9. Chiedi se si vuole sovrascrivere il TXT o no.'''

import numpy as np

while True:
    risposta = int(input("\nScrivi 1 se vuoi procedere, 0 se vuoi uscire: "))

    if risposta == 0:
        break

    elif risposta == 1:
        arr = np.linspace(0,10,50)
        arr_casuale = np.random.random(50)
        arr_totale = arr + arr_casuale
        print("\nPrimo array:\n", arr, "\nSecondo array:\n", arr_casuale, "\nArray somma:\n", arr_totale)

        somma = np.sum(arr_totale)
        print("\nLa somma totale degli elementi dell'array somma è: ", somma)

        arr5 = arr_totale[arr_totale > 5]
        print("\nGli elementi maggiori di 5 sono:\n", arr5)
        somma5 = np.sum(arr5)
        print("\nLa somma degli elementi maggiori di 5 è: ", somma5)
        
        while True:
            scelta = input("Vuoi sovrascrivere il file txt? (si/no) ")
            if scelta == "si":
                modo = "w"
                break
            elif scelta == "no":
                modo = "a"
                break
            else:
                print("Scelta non valida.")
                continue

        with open ("dati.txt", modo) as file:
            file.write("\n=== NUOVO INSERIMENTO ===\n")
            file.write("\nArray con linspace:\n" + str(arr) + "\n")
            file.write("\nArray generato casualmente:\n" + str(arr_casuale) + "\n")
            file.write("\nArray somma:\n" + str(arr_totale) + "\n")
            file.write("\nSomma degli elementi dell'array totale: " + str(somma) + "\n")
            file.write("\nArray con elementi maggiori di 5:\n" + str(arr5) + "\n")
            file.write("\nSomma degli elementi maggiori di 5: " + str(somma5) + "\n")

        print("\nDati salvati correttamente sul file dati.txt")

    else:
        print("\nRisposta non valida. Riprova!")
        continue