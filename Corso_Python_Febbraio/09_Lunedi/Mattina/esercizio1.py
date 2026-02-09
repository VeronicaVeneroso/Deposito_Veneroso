import math

# Classe Punto.
# Attributi: coordinate.
# Metodi: - spostamento di un punto di quantità date in input
# - distanza dall'origine
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)



risposta = "si"
# Finché l'utente vuole, si inseriscono nuovi punti di cui si stampa
# la distanza dall'origine e poi si sposta chiedendo all'utente di quanto.
while risposta == "si":
    risposta = input("Vuoi inserire un nuovo punto? (si/no) ")
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            continue
    print("Nuovo punto. Inserisci x:")
    x = float(input())
    print("Inserisci y:")
    y = float(input())
    punto = Punto(x,y)
    distanza = punto.distanza_da_origine()
    print("La distanza del punto dato dall'origine è ", distanza)
    print("Spostamento punto. Inserisci variazione per x:")
    dx = float(input())
    print("Inserisci variazione per y:")
    dy = float(input())
    punto.muovi(dx, dy)
    print("Il punto modificato avrà coordinate:", punto.x, "e", punto.y)

    

# EXTRA: Andare a gestire nel primo esercizio X punti che sono X oggetti che deve definire tutti e stampare tutti assieme.