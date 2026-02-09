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


# Classe biblioteca.
# Metodi: - crea_libro richiama la classe Libro
# - stampa_libro stampa la descrizione del libro
class Biblioteca:
    def crea_libro(self, titolo, autore, pagine):
        return Libro(titolo, autore, pagine)
    
    def stampa_libro(self, libro:Libro):
        libro.descrizione()


mia_biblioteca = Biblioteca()
risposta = "si"
# Ciclo di creazione e stampa di nuovi libri utilizzando i metodi della
# classe Biblioteca.
while risposta == "si":
    risposta = input("Vuoi aggiungere un libro? (si/no) ").lower()
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            risposta = "si"
            continue
    titolo = input("Inserisci titolo: ")
    autore = input("Inserisci autore: ")
    pagine = int(input("Inserisci numero di pagine: "))
    libro = mia_biblioteca.crea_libro(titolo, autore, pagine)
    mia_biblioteca.stampa_libro(libro)


