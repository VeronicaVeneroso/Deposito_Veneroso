import numpy as np
import random
'''Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D.
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie
operazioni sulla matrice. Le operazioni disponibili includono, ogni volta che il sistema
conclude un calcolo va salvato su un file txt:
1.Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
2.Estrarre e stampare la sotto-matrice centrale.
3.Trasporre la matrice e stamparla.
4.Calcolare e stampare la somma di tutti gli elementi della matrice.
5.Uscire dal programma o ripetere .'''


while True:
    scelta = int(input("\nScrivi 1 per eseguire una nuova operazione, 0 per uscire: "))
    if scelta == 0:
        break

    elif scelta == 1:
        righe = random.randint(1,10)
        colonne = random.randint(1,10)
        mat = np.random.randint(0,100,righe * colonne).reshape(righe, colonne)
        print("\nLa matrice generata ha", righe, "righe e", colonne, "colonne:\n", mat)

        with open ("matrici.txt", "a") as file:
            file.write("\n=== NUOVO INSERIMENTO ===\n")
            file.write("\nNuova matrice generata con " + str(righe) + " righe e " + str(colonne) + "colonne:\n" + str(mat))

        operazione = int(input("\nSeleziona l'operazione che vuoi eseguire sulla matrice:\n1) Estrarre la sotto-matrice centrale"
                               "\n2) Trasporre la matrice\n3) Somma di tutti gli elementi della matrice\n"
                               "4) Crea una seconda matrice e moltiplica elemento per elemento\n"
                               "5) Calcola media degli elementi della matrice\n"
                               "6) Calcola il determinante della matrice\n"))
        
        if operazione == 1:
            centro_r = righe // 2
            centro_c = colonne // 2
            
            if centro_r < 3 or centro_c < 3:
                print("\nMatrice troppo piccola per estrarre una sottomatrice centrale!")
                with open ("matrici.txt", "a") as file:
                    file.write("\nMatrice troppo piccola per estrarre una sottomatrice centrale!")
            
            else:
                sottomat = mat[centro_r - 1 : centro_r + 2, centro_c - 1 : centro_c + 2]
                print(sottomat)
                with open ("matrici.txt", "a") as file:
                    file.write("\nLa sottomatrice centrale è: " + str(sottomat))
        
        elif operazione == 2:
            trasp = mat.T
            print("\nLa matrice trasposta è:\n", trasp)
            with open ("matrici.txt", "a") as file:
                file.write("\nLa matrice trasposta è: " + str(trasp))
        
        elif operazione == 3:
            somma = np.sum(mat)
            print("\nLa somma degli elementi della matrice è: ", somma)
            with open ("matrici.txt", "a") as file:
                file.write("\nLa somma degli elementi della matrice è: " + str(somma))
        
        elif operazione == 4:
            mat2 = np.random.randint(0,100,righe * colonne).reshape(righe, colonne)
            print("\nLa seconda matrice creata è:\n", mat2)
            mat_prodotto = mat * mat2
            print("\nLa matrice prodotto è:\n", mat_prodotto)
            with open ("matrici.txt", "a") as file:
                file.write("\nSeconda matrice creata:\n" + str(mat2))
                file.write("\nProdotto tra le due matrici: " + str(mat_prodotto))
        
        elif operazione == 5:
            media = mat.mean()
            print("\nLa media degli elementi della matrice è: ", media)
            with open ("matrici.txt", "a") as file:
                file.write("\nLa media degli elementi della matrice è: " + str(media))
        
        elif operazione == 6:
            if righe == colonne:
                det = np.linalg.det(mat)
                with open ("matrici.txt", "a") as file:
                    file.write("\nDeterminante della matrice: " + str(det))
                    
            else:
                print("Non si può calcolare il determinante di una matrice non quadrata.")
                with open ("matrici.txt", "a") as file:
                    file.write("\nNon si puo' calcolare il determinante di una matrice non quadrata")

        else:
            print("\nOperazione selezionata non valida.")

    else:
        print("\nScelta selezionata non valida. Riprova!")
        continue

'''Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
1.Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una
seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per
elemento e stampare il risultato.
2.Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di
tutti gli elementi della matrice.
EXTRA:
Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la
matrice è quadrata).'''