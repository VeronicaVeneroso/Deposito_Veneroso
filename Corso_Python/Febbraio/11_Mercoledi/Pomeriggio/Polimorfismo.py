class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")
    

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")


class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")