'''Scrivete un programma che genera 5 numeri
casuali e li salva su un file, l’utente dovrà cercare di indovinarne almeno 2 oppure
avrà perso.'''

from random import sample

def check (numero) :
    try : 
        int (numero)
        return True 
    except ValueError :
        print ("ERRORE devi inserire un numero") 
        return False

numeri = sample(range(1, 101), 5)
#print(numeri)

with open("file_numeri.txt","w") as file: 
    file.write ((",").join(map(str, numeri)))
    #file.write (str(numeri).strip("[]"))

with open("file_numeri.txt","r") as file: 
    contenuto = file.read ()

contenuto = contenuto.split (",") 
#print (contenuto)

game_over = False

for i in range (5) :
    while True : 

        n1 = input ("inserisci il primo numero ")
        if not check (n1) :
            continue
        else : 

            n2 = input ("inserisci il secondo numero ")
            if not check (n2) :
                continue

        if n1 == n2 :
            print ("ERRORE due numeri non devono essere uguali")
            continue
        break 

    if n1 in contenuto and n2 in contenuto :
        print ("hai vinto ! ") 
        game_over = True
        break
    elif n1 in contenuto or n2 in contenuto :
        print ("solo un numero è corretto")
    else :
        print ("Entrambi i numeri sono sbagliati ")
if not game_over :
    print ("Hai perso e hai finito i tentativi ! ")