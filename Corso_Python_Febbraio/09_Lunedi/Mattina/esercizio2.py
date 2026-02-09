# Classe Libro.
# Attributi: titolo, autore, pagine
# Metodi: descrizione che stampa gli attributi
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")



risposta = "si"
# Ciclo che consente all'utente di inserire nuovi libri finché vuole
# e ne stampa la descrizione
while risposta == "si":
    risposta = input("Vuoi inserire un nuovo libro? (si/no) ")
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            continue
    titolo = input("Inserisci titolo: ")
    autore = input("Inserisci autore: ")
    pagine = int(input("Inserisci numero di pagine: "))
    libro = Libro(titolo, autore, pagine)
    libro.descrizione()
