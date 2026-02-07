
utenti = []
eta = []
codici = []
risposta = True
while risposta == True:
    scelta = input("Vuoi inserire un nuovo utente? (si/no) ").lower()
    match scelta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            continue

    cf = str()
    while not(len(cf) == 16):
        cf = input("Inserisci codice fiscale:\n")
        if len(cf) != 16:
            print("Il codice fiscale inserito non è corretto. Deve avere 16 caratteri. Riprova:")

    if cf in codici:
        print("Utente già registrato.")
    else:
        codici.append(cf)
        print("Inserisci età:")
        anni = int(input())
        if anni < 0 or anni > 120:
            print("Età non valida.")
            continue
        nome = input("Inserisci nome:\n")
        cognome = input("Inserisci cognome:\n")
        eta.append(anni)
        utente = (cognome, nome, anni, cf)
        utenti.append(utente)
        print("Nuovo utente inserito correttamente.")

numero_utenti = len(utenti)
if numero_utenti > 0:
    print("Ci sono ", numero_utenti, "utenti. La lista completa è:")

    for i in range(numero_utenti):
        print(i+1,  utenti[i])

    insieme_eta = set(eta)
    print("Le età degli utenti sono: ", insieme_eta)

    somma = 0
    for num in eta:
        somma = somma + num
    media = somma / numero_utenti
    print("L'età media degli utenti è", media)
else:
    print("Non ci sono utenti.")
