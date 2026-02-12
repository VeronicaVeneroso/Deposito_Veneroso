class Posto:
    def __init__(self, numero:int, fila:str):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    def get_numero(self):
        return self._numero
    
    def get_fila(self):
        return self._fila

    def get_occupato(self):
        return self._occupato
    
    def set_occupato(self, occupato:bool):
        self._occupato = occupato

    def prenota(self):
        if self.get_occupato() == False:
            self.set_occupato(True)
            print(f"Prenotazione posto numero {self.get_numero()} fila {self.get_fila()} effettuata")
        else:
            print("Posto già occupato")

    def libera(self):
        if self.get_occupato() == True:
            self.set_occupato(False)
            print(f"Il posto {self.get_numero()} fila {self.get_fila()} ora è libero")
        else:
            print("Il posto è già libero.")
    
    def __str__(self):
        return f"numero {self.get_numero()} fila {self.get_fila()}"

class PostoStandard(Posto):
    def __init__(self, numero:int, fila:str, costo:float):
        super().__init__(numero, fila)
        self.costo = costo

    def prenota(self):
        if self.get_occupato() == False:
            self.set_occupato(True)
            print(f"Prenotazione posto numero {self.get_numero()} fila {self.get_fila()} effettuata per un costo di {self.costo}€")
        else:
            print("Posto già occupato")


class PostoVIP(PostoStandard):
    def __init__(self, numero, fila, costo, servizi_extra:list):
        super().__init__(numero, fila, costo)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if self.get_occupato() == False:
            self.set_occupato(True)
            print(f"Prenotazione posto numero {self.get_numero()} fila {self.get_fila()} effettuata per un costo di {self.costo}€")
            print(f"Servizi extra attivati: {self.servizi_extra}")
        else:
            print("Posto già occupato")




class Teatro:
    def __init__(self):
        self._posti = {}
        
    def get_posti(self):
        return self._posti
    
    def set_posti(self, posti:dict[Posto]):
        self._posti = posti

    def aggiungi_posto(self, posto:Posto):
        chiave = (posto.get_numero(), posto.get_fila())
        self._posti[chiave] = posto

    def prenota_posto(self, numero:int, fila:str):
        posto = self._posti.get((numero, fila))
        if posto:
            posto.prenota()
        else:
            print("Posto non esistente")

    def stampa_posti_occupati(self):
        print("I posti occupati sono:")
        nessuno = False
        for posto in self._posti.values():
            if posto.get_occupato():
                print(posto.get_numero(), "-", posto.get_fila())
                nessuno = True
        if not nessuno:
            print("Nessun posto occupato")
        
    def stampa_posti_liberi(self):
        print("I posti liberi sono:")
        nessuno = False
        for posto in self._posti.values():
            if not posto.get_occupato():
                print(posto.get_numero(), "-", posto.get_fila())
                nessuno = True
        if not nessuno:
            print("Nessun posto libero")


teatro = Teatro()
for i in range(1,5):
    for l in range(1,3):
        posto = Posto(i,str(l))
        teatro.aggiungi_posto(posto)

print("Elenco totale posti del teatro:")
for posto in teatro.get_posti().values():
    print(posto)

costo_VIP = 25
servizi_extra = ["accesso al lounge", "servizio in posto"]

risposta = "si"
while risposta == "si":
    risposta = input("Vuoi effettuare una nuova operazione? (si/no) ")
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            risposta = "si"
            print("Opzione selezionata non valida")
            continue
    
    scelta = input("Vuoi effettuare una prenotazione o una cancellazione? (prenotazione/cancellazione) ").lower()
    match scelta:
        case "prenotazione":
            print(teatro.stampa_posti_liberi())
            fila = input("Inserisci la fila del posto che vuoi prenotare: ")
            numero = int(input("Inserisci il numero del posto che vuoi prenotare: "))
            VIP = input(f"I servizi extra offerti dal posto VIP sono {servizi_extra}. Vuoi usufruirne per un prezzo aggiuntivo di {costo_VIP}? (si/no) ").lower()
            match VIP:
                case "si":
                    pass
                case "no":
                    pass
                case _:
                    print("Opzione selezionata non valida")
        case "cancellazione":
            pass
        case _:
            print("Opzione selezionata non valida.")