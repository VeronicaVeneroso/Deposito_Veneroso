x = 10
y = 20

# condizione if
if x < y: # La condizione si può scrivere anche in parentesi
    print("Bravo")

numero = 10
# condizione if-else
if numero > 0:
    print("Il numero è positivo")
else:
    print("Blocco Else")

num = 20
# condizione if-elif-else
if num > 0:
    print("Il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
else:
    print("Il numero è zero")

# Controllo sulle stringhe
parola = "Veronica"
if parola.lower() == "veronica":
    print("Sono lo stesso nome")

if parola.lower() != "Mirko": # controlla se sono diversi
    print("Sono diversi")

if not(parola.lower() == "Mirko"): # altro modo per controllare che siano diversi
    print("Non sono uguali")


comando = input("Inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")