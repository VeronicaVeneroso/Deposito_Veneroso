from datetime import time
from Persone import Dipendente, Amministratore

class Badge:
    def __init__(self, codice:str, attivo = True):
        self.codice = codice
        self.attivo = attivo
    
    def attiva(self):
        self.attiva = True

    def disattiva(self):
        self.attiva = False

    def verifica_validità(self):
        return self.attivo

class Turno:
    def __init__(self, inizio:time, fine:time):
        self.inizio = inizio
        self.fine = fine
    
    def verifica_orario_entrata(self, orario_corrente:time):
        if orario_corrente >= self.inizio:
            minuti_ritardo = (orario_corrente.hour*60 + orario_corrente.minute) - (self.inizio.hour*60 + self.inizio.minute)
            if minuti_ritardo > 10:
                return "Ritardo"
            else:
                return "In orario"
        
    def verifica_orario_uscita(self, orario_corrente:time):
        if orario_corrente >= self.fine:
            minuti_extra = (orario_corrente.hour*60 + orario_corrente.minute) - (self.fine.hour*60 + self.fine.minute)
            if minuti_extra > 10:
                return "Straordinario effettuato"
        else:
            return "Uscita anticipata"

    
class Accessi:
    def __init__(self, registro:dict):
        self.registro = registro
    
    def registra_accesso(self, dipendente:Dipendente, orario_corrente:time, turno:Turno):
        self.registro["Entrata:"] = [dipendente.cognome, dipendente.nome, "Orario di ingresso: ", orario_corrente, turno.verifica_orario_entrata]
    
    def registra_uscita(self, dipendente:Dipendente, orario_corrente:time, turno:Turno):
        self.registro["Uscita:"] = [dipendente.cognome, dipendente.nome, "Orario di uscita: ", orario_corrente, turno.verifica_orario_uscita]
    
    def mostra_registro(self):
        print(self.registro)
    


