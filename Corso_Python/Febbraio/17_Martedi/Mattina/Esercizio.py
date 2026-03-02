'''Scrivete un gioco in cui il giocatore 1 inserisce un
numero da 1 a 100 e il giocatore2 ha 5 tentativi per
indovinare il numero.
Il programma fornisce suggerimenti (troppo alto,
troppo basso), termina quando l'utente indovina
correttamente, quando i tentativi finiscono o se
scrive «mi arrendo».'''

import random

print("---sfida---")

ncasuale = random.randint(1,100)
vite =0 

while vite<5:

    scelta = input("vuoi provare a giocare con un numero?  inserisci o scrivi arrendi:   " ).lower()

    if not  scelta.isdigit():

     if scelta =="arrendi":

       print("ti sei arreso")
       break
     else:
        print("inserisci numero o arrendi")
    else:

        n= int(scelta)

        if n ==ncasuale:
            print("hai indovinato")
            break

        elif n<ncasuale:
            print("il numero inserito e' piu basso")


        else:
            print("il numero inserito e' piu' alto")


    vite+=1

else:
    print("hai finito la vita")