'''creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento.
Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare
i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi: effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.'''


# Classe generica MetodoPagamento
# Metodi: effettua_pagamento con controllo di importo positivo
class MetodoPagamento:
    def effettua_pagamento(self, importo:float):
        if importo >= 0:
            print(f"Pagamento di {importo}€ effettuato")
        else:
            print("L'importo deve essere positivo")

# Classe CartaDiCredito
# Attributi: numero_carta con controllo sul numero di cifre
# Metodi: effettua_pagamento con controllo di importo positivo
class CartaDiCredito:
    def __init__(self, numero_carta: str):
        if len(numero_carta) == 16:
            self.numero_carta = numero_carta
        else:
            print("Il numero di carta deve essere composto da 16 cifre")

    def effettua_pagamento(self, importo:float):
        if importo >= 0:
            print(f"Pagamento di {importo}€ effettuato con carta di credito numero {self.numero_carta}")
        else:
            print("L'importo deve essere positivo")

# Classe PayPal
# Attributi: email
# Metodi: effettua_pagamento con controllo di importo positivo
class PayPal:
    def __init__(self, email:str):
        self.email = email

    def effettua_pagamento(self, importo:float):
        if importo >= 0:
            print(f"Pagamento di {importo}€ effettuato tramite PayPal dall'account {self.email}")
        else:
            print("L'importo deve essere positivo")


# Classe BonificoBancario
# Attributi: iban con controllo della lunghezza
# Metodi: effettua_pagamento con controllo di importo positivo
class BonificoBancario:
    def __init__(self, iban:str):
        if len(iban) == 27:
            self.iban = iban
        else:
            print("L'iban deve contenere 27 caratteri")

    def effettua_pagamento(self, importo:float):
        if importo >= 0:
            print(f"Bonifico di {importo}€ effettuato dall'IBAN {self.iban}")
        else:
            print("L'importo deve essere positivo")


# Classe GestorePagamenti
# Attributi: metodo
# Metodi: pagamento con controllo di importo positivo e richiamo del metodo effettua_pagamento
class GestorePagamenti:
    def __init__(self, metodo:object):
        self.metodo = metodo

    def pagamento(self, importo:float):
        if importo >= 0:
            self.metodo.effettua_pagamento(importo)
        else:
            print("L'importo deve essere positivo")


import random

risposta = "si"
# inizializzazione metodi dell'utente
metodi = [CartaDiCredito("5246548652453652"), PayPal("utente@email.com"), BonificoBancario("IT2565462536524512563256487")]
# Ciclo per ripetere le operazioni quante volte vuole l'utente
while risposta == "si":
    risposta = input("Vuoi effettuare un nuovo pagamento? (si/no) ")
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Opzione non disponibile")
            risposta = "si"
            continue
    
    # inserimento importo pagamento
    importo = float(input("Inserisci importo del pagamento "))
    # richiamo di GestorePagamenti con un metodo scelto randomicamente
    gestore = GestorePagamenti(random.choice(metodi))
    # pagamento con metodo scelto
    gestore.pagamento(importo)
