class Utente:
    pwd_segreta = "itopinonavevanonipoti"
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
    
    def accesso(self):
        if self.password == self.pwd_segreta:
            print("Sei un amministratore!")
            amministratore = True
        else:
            print("Sei un cliente!")
            amministratore = False
    
    def effettua_acquisto(self):


class Negozio:
    def __init__(self, nome, inventario:dict):
        self.nome = nome
        self.inventario = inventario

    def aggiorna_inventario(self, prodotto, prezzo, quantità):
        self.inventario[prodotto] ={"Prezzo": prezzo, "Quantità": quantità}

    def mostra_inventario(self):
        print(self.inventario.items())
        

risposta = "si"
# Ciclo che permette di accedere tante volte quante vuole l'utente
while risposta == "si":
    risposta = input("Vuoi effettuare un nuovo accesso? (si/no) ").lower()
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            risposta = "si"
            continue

    scelta = input("Sei un utente o un negozio? (utente/negozio) ").lower()
    match scelta:
        case "utente":
            nome = input("Inserisci nome utente: ")
            password = input("Inserisci password: ")
            utente = Utente(nome, password)
            utente.accesso()
        
        case "negozio":
            nome = input("Inserisci nome negozio: ")
            azione = input("Vuoi aggiornare o visualizzare l'inventario? (aggiornare/visualizzare)").lower()
            
