class umano():
    def cammina(self):
        print("sto camminando su due zampe")

class struzzo():
    def cammina(self):
        print("sto camminando su due zampe")


u = umano()
s = struzzo()

def cammina(elemento:object):
    elemento.cammina()


class Cane:
    def parla(self):
        return "Bau!"
    
class Gatto:
    def parla(self):
        return "Miao!"

def fai_parlare(animale):
    # Non importa che tipo sia l'animale,
    print(animale.parla())

cane = Cane()
gatto = Gatto()

fai_parlare(cane) # Output: Bau!
fai_parlare(gatto) # Output: Miao!


class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")

def disegna_figura(figura):
    # Anche qui basta che "figura" abbia il metodo "disegna"
    figura.disegna()

figure = [Cerchio(), Rettangolo()]

for figura in figure:
    disegna_figura(figura)