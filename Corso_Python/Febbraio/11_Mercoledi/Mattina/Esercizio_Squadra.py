# Creare una classe base MembroSquadra e una Squadra che conterrà
# le diverse classi figlie che rappresentano ruoli specifici all'interno
# della squadra di calcio, come Giocatore, Allenatore e Assistente.
# Classe MembroSquadra:
# Attributi: nome(str), età(int)
# Metodi: descrivi()(stampa una descrizione generale del membro della squadra)
# Classi derivate:
# Giocatore:
# Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
# Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
# Allenatore:
# Attributi aggiuntivi come anni_di_esperienza
# Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
# Assistente:
# Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
# Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team
# Crea due squadre e falle giocare contro.

import random

# classe padre MembroSquadra.
# attributi: nome e età
# metodi: descrivi (descrive gli attributi del singolo membro)
class MembroSquadra:
    def __init__(self, nome:str, età:int):
        self.nome = nome
        self.età = età

    def descrivi(self):
        return f"{self.nome} ha {self.età} anni"


# classe Giocatore.
# attributi: nome, età, ruolo e numero di maglia
# metodi: descrivi (dà una descrizione generale di tutti gli attributi del giovatore),
# gioca partita (attribuisce un'azione random al giocatore tra le azioni disponibili)
class Giocatore(MembroSquadra):
    def __init__(self, nome:str, età:int, ruolo:str, numero_maglia:int):
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        return f"{super().descrivi()}, gioca nel ruolo {self.ruolo} con il numero {self.numero_maglia}"

    def gioca_partita(self):
        possibili_azioni = [
            "segna un goal",
            "fa un assist decisivo",
            "recupera la palla con un grande intervento",
            "sbaglia un tiro facile",
            "fa un passaggio perfetto"
        ]
        azione = random.choice(possibili_azioni)
        return f"{self.nome} {azione}"

# classe Allenatore.
# attributi: nome, età, anni di esperienza, punto di forza
# metodi: descrivi (dà una descrizione generale di tutti gli attributi dell'allenatore),
# dirige allentamento (descrive su quali punti di forza si basa il tipo di allenamento dell'allenatore),
class Allenatore(MembroSquadra):
    def __init__(self, nome:str, età:int, anni_di_esperienza:int, punto_di_forza:str):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esperienza
        self.punto_di_forza = punto_di_forza

    def descrivi(self):
        return f"{super().descrivi()} ed è un allenatore con {self.anni_di_esperienza} anni di esperienza"

    def dirige_allenamento(self):
        return f"dirige un allenamento intenso basato su {self.punto_di_forza}"

# classe Assistente.
# attributi: nome, età, specializzazione
# metodi: descrivi (dà una descrizione generale degli attributi dell'assistente),
# supporta_team (dichiara qual è il tipo di specializzazione dell'assistente e in che modo supporta la squadra)
class Assistente(MembroSquadra):
    def __init__(self, nome:str, età:int, specializzazione:str):
        super().__init__(nome, età)
        self.specializzazione = specializzazione

    def descrivi(self):
        return f"{super().descrivi()} ed è un assistente specializzato in {self.specializzazione}"

    def supporta_team(self):
        return f"{self.nome} supporta la squadra come {self.specializzazione}"

# classe Squadra
# attributi: nome, membri della squadra, goal fatti
# metodi: aggiungi_membro (permette di aggiungere membri alla squadra),
# descrivi_squadra (stampa le descrizioni di tutti i membri della squadra)
# gioca_partita(stampa un'azione effettuata da ogni giocatore della squadra e incrementa il numero di goal
# se l'azione effettuata è un goal),
# mostra_risultato (restituisce il numero di goal effettuati dalla squadra)
class Squadra:
    def __init__(self, nome:str):
        self.nome = nome
        self.membri: list[MembroSquadra] = []
        self.goal = 0
    
    def aggiungi_membro(self, membro:MembroSquadra):
        self.membri.append(membro)
    
    def descrivi_squadra(self):
        print(f"Presentazione della squadra {self.nome}:")
        for membro in self.membri:
            print(membro.descrivi())
    
    def gioca_partita(self):
        print(f"{self.nome} scende in campo!")
        for membro in self.membri:
            if isinstance(membro, Giocatore):
                evento = membro.gioca_partita()
                print(evento)
                if "goal" in evento:
                    self.goal += 1
    
    def mostra_risultato(self):
        return self.goal
    

risposta = "si"
# Ciclo ripetibile per giocare quante partite vuole l'utente
while risposta == "si":
    risposta = input("Vuoi giocare una partita? (si/no) ").lower()
    if risposta == "si":
        pass
    elif risposta == "no":
        break
    else:
        print("Risposta non valida.")
        risposta = "si"
        continue

    # scelta dei nomi delle squadre
    nome1 = input("\nScegli il nome della squadra 1: ")
    squadra1 = Squadra(nome1)
    nome2 = input("\nScegli il nome della squadra 2: ")
    squadra2 = Squadra(nome2)

    # creazione prima squadra
    print("\nCrea la prima squadra. Inserisci 2 giocatori.")
    for i in range(2):
        nome = input("\nInserisci il nome del nuovo giocatore: ")
        età = int(input("Quanti anni ha? "))
        ruolo = input("In che ruolo gioca? ")
        numero = int(input("Qual è il numero della sua maglia? "))
        squadra1.aggiungi_membro(Giocatore(nome, età, ruolo, numero))
    
    nome = input("\nInserisci il nome dell'allenatore: ")
    età = int(input("Quanti anni ha? "))
    esperienza = int(input("Quanti anni di esperienza ha? "))
    punto_di_forza = input("Qual è il suo punto di forza? ")
    squadra1.aggiungi_membro(Allenatore(nome, età, esperienza,punto_di_forza))

    nome = input("\nInserisci il nome dell'assistente: ")
    età = int(input("Quanti anni ha? "))
    specializzazione = input("Qual è la sua specializzazione? ")
    squadra1.aggiungi_membro(Assistente(nome, età, specializzazione))

    # creazione seconda squadra
    print("\nCrea la seconda squadra. Inserisci 2 giocatori.")
    for i in range(2):
        nome = input("\nInserisci il nome del nuovo giocatore: ")
        età = int(input("Quanti anni ha? "))
        ruolo = input("In che ruolo gioca? ")
        numero = int(input("Qual è il numero della sua maglia? "))
        squadra2.aggiungi_membro(Giocatore(nome, età, ruolo, numero))
    
    nome = input("\nInserisci il nome dell'allenatore: ")
    età = int(input("Quanti anni ha? "))
    esperienza = int(input("Quanti anni di esperienza ha? "))
    punto_di_forza = input("Qual è il suo punto di forza? ")
    squadra2.aggiungi_membro(Allenatore(nome, età, esperienza,punto_di_forza))

    nome = input("\nInserisci il nome dell'assistente: ")
    età = int(input("Quanti anni ha? "))
    specializzazione = input("Qual è la sua specializzazione? ")
    squadra2.aggiungi_membro(Assistente(nome, età, specializzazione))

    # inizio partita: entrambe le squadre fanno il loro gioco
    print("\nIniziamo la partita\n")
    squadra1.gioca_partita()
    squadra2.gioca_partita()

    # stampa risultato finale
    print(f"\nRISULTATO FINALE: {squadra1.nome} {squadra1.mostra_risultato()} - {squadra2.mostra_risultato()} {squadra2.nome}")

    # dichiara l'eventuale vincitore o la parità in base al numero di goal effettuati dalle due squadre
    if squadra1.goal > squadra2.goal:
        print(f"\nVince {squadra1.nome}!")
    elif squadra2.goal > squadra1.goal:
        print(f"\nVince {squadra2.nome}!")
    else:
        print("\nPareggio!")