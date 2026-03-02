# esercizio 1: Creare una serie di condizioni una dentro l’altra che a fronte di un
# input per ogni if decidano se farti passare o no (3 livelli, fate un
# paragone con ==)

# Chiedere all'utente se è iscritto
iscrizione = input("Sei iscritto? (si/no) ")

# Controllo dell'iscrizione
if iscrizione == "si":
    abbonamento = input("Hai pagato l'abbonamento di questo mese? (si/no) ")
    
    # Controllo del pagamento dell'abbonamento
    if abbonamento == "si":
        documento = input("Hai il documento? (si/no) ")
        
        # Controllo documento
        if documento == "si":
            print("Accesso consentito")

        else:
            print("Accesso negato per assenza di documento")
    else:
        print("Accesso negato per mancato pagamento")
else:
    print("Accesso negato per mancata iscrizione")



# esercizio 2: Andare a creare un if con vari elif e un else finale che gestisca un
# menu per la selezione di un crud basilare (aggiungi rimuovi elimina)

# lista nomi già esistente
lista_nomi = ["Veronica", "Gianluca", "Patrizia"]
# stampa le opzioni disponibili per l'utente
print("1 - Aggiungi nuovo utente\n2 - Rimuovi un utente\n3 - Elimina tutto")

# far selezionare l'operazione da eseguire all'utente
risposta = input("Seleziona l'operazione da eseguire: ")

# prima opzione: aggiungere elemento alla lista
if risposta == "1":
    nome = input("Inserisci nome da aggiungere: ")
    lista_nomi.append(nome)
    print(lista_nomi)
# seconda opzione: rimuovere un elemento dalla lista
elif risposta == "2":
    nome = input("Indica il nome da rimuovere: ")
    if nome in lista_nomi:
        lista_nomi.remove(nome)
    print(lista_nomi)
# terza opzione: cancellare l'intera lista
elif risposta == "3":
    lista_nomi.clear()
    print("Lista cancellata")
# se l'input non rientra tra le 3 opzioni elencate non procede
else:
    print("Operazione non valida")



# esercizio 3: Creare un if con else semplice, dentro l’if inserire una struttura di
# creazione di dati (nome, password, id dato dal sistema a crescere) e
# nell’else il controllo automatico laddove è presente l’accout nel sistema
# e solo se si passa dall’else concludere lo script

# lista utenti già esistenti
utenti = ["Veronica"]
# inizializzazione id per il prossimo utente da aggiungere
id = len(utenti)+1

# Far inserire all'utente il suo nickname
nickname = input("Inserisci il tuo nickname: ")

# Se il nickname non esiste già nella lista ne crea uno nuovo e lo stampa
if nickname not in utenti:
    utenti.append(nickname)
    print("Account creato! Id: ", id, "Nickname: ", nickname)
    print("La lista completa degli utenti è: ", utenti)
    id = id + 1
# Se il nickname già esiste non lo crea e finisce
else:
    print("Nickname già esistente!")
    print("Fine")