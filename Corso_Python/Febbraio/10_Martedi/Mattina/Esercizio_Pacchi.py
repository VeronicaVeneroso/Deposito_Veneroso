'''Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato
(es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.
Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco,
cercarlo per codice, e mostrare tutti i pacchi in un certo stato.
Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”,
segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.
Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi
(almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi
“in consegna” e il peso totale dei pacchi non ancora consegnati.'''

# classe Pacco. Attributi: codice, peso e stato
class Pacco:
    def __init__(self, codice:str, peso:float, stato:str):
        self.codice = codice
        self.peso = peso
        self.stato = stato
    
    # funzione che mostra tutte le info di un singolo pacco
    def mostra_info(self):
        print(f"Pacco: {self.codice}, peso: {self.peso} kg, stato: {self.stato}")
    
    # funzione che cambia lo stato di un pacco
    def cambia_stato(self, stato):
        self.stato = stato

# classe Magazzino. Attributi: un dizionario di pacchi
class Magazzino:
    def __init__(self):
        self.pacchi = {}
    
    # funzione che permette di aggiungere un oggetto di tipo Pacco al dizionario
    def aggiungi_pacco(self, pacco:Pacco):
        self.pacchi[pacco.codice] = pacco
    
    # funzione che consente di cercare un pacco nel dizionario e restituisce le info del pacco
    def cerca_pacco(self, codice:str):
        if codice in self.pacchi:
            return self.pacchi[codice]
        else:
            print("Il pacco non è presente in magazzino.")
            return None
    
    # funzione che mostra tutti i pacchi che sono in un determinato stato
    def mostra_pacchi_per_stato(self, stato:str):
        for pacco in self.pacchi.values():
            if pacco.stato == stato:
                pacco.mostra_info()


# classe GestorePacchi. Attributi: magazzino.
class GestorePacchi:
    def __init__(self, magazzino:Magazzino):
        self.magazzino = magazzino

    # funzione che mette un determinato pacco in consegna se presente in magazzino.
    def metti_in_consegna(self, codice:str):
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco.stato == "in magazzino":
            pacco.cambia_stato("in consegna")
        else:
            print("Il pacco non è presente in magazzino.")

    # funzione che imposta lo stato di un pacco in "consegnato" se presente tra quelli in consegna.
    def pacco_consegnato(self, codice:str):
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco.stato == "in consegna":
            pacco.cambia_stato("consegnato")
        else:
            print("Il pacco non è tra quelli in consegna.")

    # funzione che restituisce il peso totale dei pacchi che non sono ancora stati consegnati.
    def peso_totale_non_consegnato(self):
        totale = 0
        for pacco in self.magazzino.pacchi.values():
            if pacco.stato != "consegnato":
                totale += pacco.peso
        return totale
    

# Inizializzazione magazzino e gestore magazzino
magazzino = Magazzino()
gestore = GestorePacchi(magazzino)

# creazione nuovi pacchi
pacco1 = Pacco("0001", 1, "in magazzino")
pacco2 = Pacco("0002", 5, "in consegna")
pacco3 = Pacco("0003", 2, "in magazzino")
pacco4 = Pacco("0004", 3.5, "in consegna")
pacco5 = Pacco("0005", 2.5, "in magazzino")

# creazione magazzino con aggiunta di tutti i pacchi creati.
for pacco in [pacco1, pacco2, pacco3, pacco4, pacco5]:
    magazzino.aggiungi_pacco(pacco)

# spostamento di alcuni pacchi da uno stato al successivo.
gestore.metti_in_consegna("0001")
gestore.pacco_consegnato("0002")
gestore.metti_in_consegna("0005")

# stampa pacchi in magazzino
print("\nPACCHI IN MAGAZZINO:")
magazzino.mostra_pacchi_per_stato("in magazzino")

# stampa pacchi in consegna
print("\nPACCHI IN CONSEGNA:")
magazzino.mostra_pacchi_per_stato("in consegna")

# stampa peso totale di pacchi ancora da consegnare
print(f"\nIl peso totale dei pacchi ancora da consegnare è {gestore.peso_totale_non_consegnato()} kg.")