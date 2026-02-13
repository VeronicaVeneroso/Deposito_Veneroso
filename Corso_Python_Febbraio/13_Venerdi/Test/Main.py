from datetime import time
from Persone import Dipendente, Amministratore
from Accesso import Badge, Turno, Accessi

# Inizializzazioni
turno = Turno(time(9,0), time(17,0))
registro = {}
accessi = Accessi(registro)
badge1 = Badge("B001", attivo=True)
badge2 = Badge("B002", attivo=True)
badge3 = Badge("B003", attivo=False)
dipendente1 = Dipendente("Veronica", "Veneroso", "001", turno, badge1)
dipendente2 = Dipendente("Michele", "Rossi", "002", turno, badge2)
amministratore = Amministratore("Giulio", "Bianchi", "003", turno, badge3)

# stampa tutti gli accessi
print("Ingressi:")
orario_ingresso = time(9,5)
for persona in [dipendente1, dipendente2, amministratore]:
    accessi.registra_accesso(persona, orario_ingresso, persona.turni)
    print(persona.descrivi())

# stampa tutte le uscite
print("\nUscite:")
orario_uscita = time(17,15)
for persona in [dipendente1, dipendente2, amministratore]:
    accessi.registra_uscita(persona, orario_uscita, persona.turni)
    print(persona.descrivi())

# stampa tutto il registro
print("\nRegistro accessi:")
accessi.mostra_registro()