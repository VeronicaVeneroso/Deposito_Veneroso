class Negozio:
    def __init__(self, nome, inventario:dict):
        self.nome = nome
        self.inventario = inventario
        self.vendite_effettuate = 0


    def aggiungi_prodotto_in_inventario(self, prodotto, prezzo, quantità):
        self.inventario[prodotto] = {
            "prezzo": prezzo,
            "quantità": quantità
            }

    def rimuovi_prodotto_da_inventario(self, prodotto):
        if prodotto in self.inventario:
            del self.inventario[prodotto]
        else:
            print("Prodotto non presente nell'inventario")

    def mostra_inventario(self):
        print("Listino prodotti disponibili")
        print(self.inventario)
    
    def aggiorna_vendite(self, prezzo):
        self.vendite_effettuate += prezzo
    
    def visualizza_vendite(self):
        print(f"Le vendite totali ammontano a {self.vendite_effettuate}")



class Utente:
    pwd_segreta = "itopinonavevanonipoti"
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
        self.amministratore = False
    
    def accesso(self):
        if self.password == self.pwd_segreta:
            print("Sei un amministratore!")
            self.amministratore = True
        else:
            print("Sei un cliente!")
            self.amministratore = False
    
    def visualizza_inventario(self, negozio:Negozio):
        negozio.mostra_inventario()

    def visualizza_vendite(self, negozio:Negozio):
        if self.amministratore:
            print(f"Le vendite totali ammontano a {negozio.vendite_effettuate}")
    
    def effettua_acquisto(self, negozio:Negozio, prodotto):
        if self.amministratore == False:
            if prodotto in negozio.inventario:
                prezzo = negozio.inventario[prodotto]["prezzo"]
                negozio.aggiorna_vendite(prezzo)
                negozio.rimuovi_prodotto_da_inventario(prodotto)
            else:
                print("Prodotto non disponibile")




inventario = {
    "Salame": {"prezzo": 10, "quantità": 3},
    "Prosciutto": {"prezzo": 15, "quantità": 5}
    }
negozio = Negozio("NomeNegozio", inventario)
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

    scelta = True
    while scelta:
        accesso = input("Sei un utente o un negozio? (utente/negozio) ").lower()
        match accesso:
            case "utente":
                scelta = False
                nome = input("Inserisci nome utente: ")
                password = input("Inserisci password: ")
                utente = Utente(nome, password)
                utente.accesso()
                utente.visualizza_inventario(negozio)
                azione = "si"
                while azione == "si":
                    azione = input("Vuoi effettuare un acquisto? (si/no) ").lower()
                    if azione == "si":
                        prodotto = input("Inserisci prodotto da acquistare: ")
                        if prodotto in inventario:
                            utente.effettua_acquisto(negozio,prodotto)

            case "negozio":
                scelta = False
        
                azione = input("Sei interessato all'inventario o alle vendite? (inventario/vendite) ").lower()
                if azione == "inventario":
                    azione_inv = input("Vuoi aggiornare o visualizzare l'inventario? (aggiornare/visualizzare) ").lower()
                    match azione_inv:
                        case "aggiornare":
                            azione_inv = input("Vuoi aggiungere o togliere un prodotto? (aggiungere/togliere) ").lower()
                            if azione_inv == "aggiungere":
                                prodotto = input("Quale prodotto vuoi inserire? ")
                                prezzo = float(input("Che prezzo ha? "))
                                quantita = int(input("Quanti pezzi hai? "))
                                negozio.aggiungi_prodotto_in_inventario(prodotto, prezzo, quantita)
                                negozio.mostra_inventario()
                            else:
                                prodotto = input("Quale prodotto vuoi rimuovere? ")
                                negozio.rimuovi_prodotto_da_inventario(prodotto)
                                negozio.mostra_inventario()

                        case "visualizzare":
                            negozio.mostra_inventario()
                elif azione == "vendite":
                    negozio.visualizza_vendite()

            case _:
                print("Opzione selezionata non valida.")