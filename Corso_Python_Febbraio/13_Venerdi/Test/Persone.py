from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nome:str, cognome:str, codice_id:str):
        if not nome or not cognome or not codice_id:
            print("Nome, cognome e codice_id non possono essere vuoti.")
        self.nome = nome
        self.cognome = cognome
        self.codice_id = codice_id

    @abstractmethod
    def descrivi(self):
        return self.nome, self.cognome, "codice_id:", self.codice_id
    
class Dipendente(Persona):
    def __init__(self, nome:str, cognome:str, codice_id:str, turni, badge):
        super().__init__(nome, cognome, codice_id)
        self.turni = turni
        self.badge = badge
    
    def descrivi(self):
        return "Dipendente", super().descrivi(), "turni: ", self.turni, "badge:", self.badge
    
class Amministratore(Dipendente):
    def descrivi(self):
        return "Amministratore", self.nome, self.cognome, "codice_id:", self.codice_id, self.turni, "badge:", self.badge