# Scrivi un programma che chieda all'utente la sua età. Se l'età è
# inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
# vedere questo film".
# Altrimenti, dovrebbe stampare "Puoi vedere questo film".

# Permette all'utente di inserire la sua età
eta = int(input("Quanti anni hai? "))

# Controllo sull'età
if eta < 18:
    utente = "minorenne"
else:
    utente = "maggiorenne"

# Se l'utente è minorenne non può vedere il film, altrimenti sì
match utente:
    case "minorenne":
        print("Mi dispiace, non puoi vedere questo film.")
    case _:
        print("Puoi vedere questo film")



# Scrivi un programma che chieda all'utente di inserire due
# numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
# moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
# l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
# per zero, il programma dovrebbe stampare "Errore: Divisione per zero".
# Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
# non valida".

# L'utente deve inserire i numeri e l'operazione da eseguire su quei numeri
x = float(input("Inserisci il primo numero: "))
y = float(input("Inserisci il secondo numero: "))
print("Le operazioni disponibili sono le seguenti:\n1 - addizione (+)\n2 - sottrazione (-)\n3 - moltiplicazione (*)\n4 - divisione (/)")
operazione = input("Scegli l'operazione: ")

# Distinzione tra le varie operazioni
match operazione:
    case "1":
        risultato = x + y
    case "2":
        risultato = x - y
    case "3":
        risultato = x * y
    case "4":
        if y != 0:
            risultato = x / y
        else:
            risultato = "Divisione per 0 non valida"
    case _:
        risultato = "Opzione selezionata non valida."
print(risultato)



# esercizio 3: match nel match

sesso = input("Inserisci il tuo sesso: (femmina/maschio) ")

match sesso:
    case "femmina":
        print("Sei femmina")
    case "maschio":
        print("Sei maschio")
    case _:
        print("Valore inserito non valido")