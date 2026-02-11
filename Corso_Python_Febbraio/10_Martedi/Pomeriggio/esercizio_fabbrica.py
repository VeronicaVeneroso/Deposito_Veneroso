class Prodotto:
    def __init__(self, nome:str, costo_produzione:float, prezzo_vendita:float):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
    

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale


class Fabbrica:
    def __init__(self):
        self.inventario = {}

    # metodo che aggiunge un prodotto all'inventario
    def aggiungi_prodotto(self, prodotto:Prodotto, quantità): 
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantità"] += quantità
        else:
            self.inventario[prodotto.nome] = {
                "costo": prodotto.costo_produzione,
                "prezzo": prodotto.prezzo_vendita,
                "quantità": quantità
            }
        print(f"{quantità} pezzi di {prodotto.nome} sono stati aggiunti all'inventario")

    # metodo che diminuisce la quantità di un prodotto in inventario
    # e stampa il profitto realizzato dalla vendita
    def vendi_prodotto(self, prodotto:Prodotto, quantità):
        if prodotto in self.inventario.keys:
            if self.inventario[prodotto.nome]["quantità"] < quantità:
                print(f"Acquisto non permesso. Quantità massima disponibile: {self.inventario[prodotto.nome]["quantità"]}")
            else:
                self.inventario[prodotto.nome]["quantità"] -= quantità
                print(f"Sono stati venduti {quantità} pezzi di {prodotto.nome}.")
        else:
            print("Prodotto non disponibile.")

    # metodo che aumenta la quantità di un prodotto restituito in inventario
    def resi_prodotto(self, prodotto:Prodotto, quantità):
        self.inventario[prodotto.nome]["quantità"] += quantità
        print(f"Sono stati resi {quantità} pezzi di {prodotto.nome}")


risposta = "si"
while risposta == "si":
    pass
