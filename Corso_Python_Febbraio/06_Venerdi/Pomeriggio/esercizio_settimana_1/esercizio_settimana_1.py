# Inizializzazione variabili
utenti = []
eta = []
codici = []
risposta = True
# Finché l'utente vuole, ripete il procedimento per riempire la lista di utenti
while risposta == True:
    scelta = input("Vuoi inserire un nuovo utente? (si/no) ").lower()
    # Procede con il codice solo se la scelta dell'utente è "si". Se risponde "no" si ferma.
    # Se la risposta è diversa da "si" e "no" ripete la domanda.
    match scelta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            continue

    # Chiede all'utente di inserire il codice fiscale e lo accetta solo se ha 16 caratteri
    cf = str()
    while not(len(cf) == 16):
        cf = input("Inserisci codice fiscale:\n")
        if len(cf) != 16:
            print("Il codice fiscale inserito non è corretto. Deve avere 16 caratteri. Riprova:")

    # Controlla se il codice fiscale è già esistente. Se non lo è richiede gli altri dati e aggiorna la lista, altrimenti non procede
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

# Stampa la lunghezza della lista
numero_utenti = len(utenti)
if numero_utenti > 0:
    print("Ci sono ", numero_utenti, "utenti. La lista completa è:")
    # Stampa la lista numerata
    for i in range(numero_utenti):
        print(i+1,  utenti[i])

    # Crea l'insieme di tutte le età degli utenti registrati nella lista
    insieme_eta = set(eta)
    print("Le età degli utenti sono: ", insieme_eta)

    # Calcola l'età media degli utenti presenti nella lista
    somma = 0
    for num in eta:
        somma = somma + num
    media = somma / numero_utenti
    print("L'età media degli utenti è", media)

# Se la lista è vuota dice che non ci sono utenti
else:
    print("Non ci sono utenti.")
