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
    def __init__(self, inventario:dict):
        self.inventario = inventario

    def aggiungi_prodotto(self):
        pass

    def vendi_prodotto(self):
        pass

    def resi_prodotto(self):
        pass