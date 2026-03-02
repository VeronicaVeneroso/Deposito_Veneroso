# Decoratore per iterare un procedimento
def ripeti_procedimento(funzione):
    def wrapper(*args, **kwargs):
        risposta = True
        while risposta == True:
            scelta = input("Vuoi inserire un nuovo utente? (si/no) ").lower()
            match scelta:
                case "si":
                    args = funzione(*args, **kwargs)
                case "no":
                    return(args)
                case _:
                    print("Risposta non valida.")
                    continue
    return wrapper


# Funzione per calcolare il valore medio degli elementi in una lista
def media(lista):
    somma = 0
    for num in lista:
        somma = somma + num
    media = somma / len(lista)
    return media

# Funzione per inserire un codice fiscale
def inserisci_cf():
    cf = str()
    while not(len(cf) == 16):
        cf = input("Inserisci codice fiscale:\n")
        if len(cf) != 16:
            print("Il codice fiscale inserito non è corretto. Deve avere 16 caratteri. Riprova:")
    return cf

# Funzione per inserire l'età
def inserisci_eta():
    anni = -1
    while anni <0 or anni > 120:
        print("Inserisci età:")
        anni = int(input())
        if anni < 0 or anni > 120:
            print("Età non valida.")
    return anni

# Funzione per inserire nome e cognome di un utente
def inserisci_nome_cognome():
    nome = input("Inserisci nome:\n")
    cognome = input("Inserisci cognome:\n")
    return nome, cognome

# Funzione per inserire i dati di un nuovo utente solo se non è già presente
# (confronta il codice fiscale con l'elenco di quelli già inseriti)
def inserisci_utente(lista):
    cf = inserisci_cf()
    if cf in lista:
        print("Utente già registrato.")
        esistenza = True
    else:
        lista.append(cf)
        anni = inserisci_eta()
        nome, cognome = inserisci_nome_cognome()
        esistenza = False
    return(esistenza, cognome, nome, anni, cf)

# Funzione che stampa la lunghezza di una lista, la lista numerata,
# le età degli utenti (come insieme) e l'età media degli utenti.
# Se la lista è vuota stampa "Non ci sono utenti"
def stampa_dati_lista(lista, eta):
    numero_utenti = len(lista)
    if numero_utenti > 0:
        print("Ci sono ", numero_utenti, "utenti. La lista completa è:")
        # stampa la lista numerata
        for i in range(numero_utenti):
            print(i+1,  lista[i])
        # Stampa di tutti i valori di età disponibili e dell'età media
        insieme_eta = set(eta)
        print("Le età degli utenti sono: ", insieme_eta)
        eta_media = media(eta)
        print("L'età media degli utenti è", eta_media)
    else:
        print("Non ci sono utenti.")
    

# Decoratore che inizializza le liste e stampa tutti i dati finali
def inizializzazione_e_stampa(funzione):
    def wrapper():
        lista = []
        eta = []
        codici = []
        lista, eta, codici = funzione(lista, eta, codici)
        stampa_dati_lista(lista, eta)
        return lista, eta, codici
    return wrapper


# Funzione per creare la lista con decoratore di iterazione e
# decoratore di inizializzazione liste e stampa di dati finali
@inizializzazione_e_stampa
@ripeti_procedimento
def crea_lista(lista, eta, codici):
    esistenza, cognome, nome, anni, cf = inserisci_utente(codici)
    if esistenza == False:
        utente = (cognome, nome, anni, cf)
        eta.append(anni)
        lista.append(utente)
        print("Nuovo utente inserito correttamente.")
    return lista, eta, codici


# Comando che chiama un'unica funzione per creare una lista di utenti
lista, eta, codici = crea_lista()