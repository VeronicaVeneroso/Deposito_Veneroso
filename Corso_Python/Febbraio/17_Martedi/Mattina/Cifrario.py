'''Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave.'''

alfabeto = "abcdefghijklmnopqrstuvwxyz"

def sposta_lettere(chiave_num, parola: str, scelta):
    # parola = parola.replace(" ", "")
    parola = parola.strip()
    nuova_parola = []
    
    if not chiave_num.isdecimal():
        print("devi inserire una parola")
        return False
    
    if scelta == "c":
    
        chiave_num = int(chiave_num)
        
        for carattere in parola.lower():
            if  carattere in alfabeto:
                indice_attuale = alfabeto.index(carattere)
                indice_new = (indice_attuale + chiave_num) %len(alfabeto)
                print(f"DEBUG: {indice_new}")
                nuova_parola.append(alfabeto[indice_new])
            else:
                nuova_parola.append(carattere)
            
        return "".join(nuova_parola)   
    
    if scelta == "d":
        
        chiave_num = int(chiave_num)
        
        for carattere in parola.lower():
            if  carattere in alfabeto:
                indice_attuale = alfabeto.index(carattere)
                indice_new = (indice_attuale - chiave_num) %len(alfabeto)
                print(f"DEBUG: {indice_new}")
                nuova_parola.append(alfabeto[indice_new])
            else:
                nuova_parola.append(carattere)
        
        return "".join(nuova_parola)
          
                
# --- PLAY ---
while True:

        scelta = input("scrivi c per criptare, d per decriptare o e per uscire: ").lower()
        
        if scelta not in ("c" , "d", "e"):
            print("ERRORE: scelta non valida")
            
        elif scelta == "e":
            print("CIAO!! ")
            break
            
        else:
            parola = input("scrivi la parola: ").lower() 
            if parola or not parola.isdigit():
        
                chiave_num = input("inserisci il numero della chiave: ")
                risultato = sposta_lettere(chiave_num, parola, scelta)

                if risultato:
                    print(f"risultato: {risultato}")