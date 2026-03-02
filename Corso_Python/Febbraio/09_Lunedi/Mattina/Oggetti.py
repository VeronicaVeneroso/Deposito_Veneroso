class Persona():
    x = 10
    def __init__(self):
        pass



O_mirko = Persona()
OBJveronica = Persona()
michele_OBJ = Persona()

print(O_mirko.x)

michele_OBJ.x = 17
print(michele_OBJ.x)
Persona.x = 20
veronica_OBJ = Persona()
print(veronica_OBJ.x)




class Automobile:
    numero_di_ruote = 4

    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)


auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()

print(auto1.marca)
print(auto2.modello)

print(type(10))
print(type(3.14))
print(type("test"))
print(type([1, 2]))


class MioOggetto:
    def __init__(self, quantita): # si può mettere quantita = 0, oppure quantita:int, ecc. Nel self non si deve mettere niente
        self.quantita = quantita

    def __str__(self):
        # Viene richiamato quando facciamo print(istanza_di_Persona)
        return "Ciao Veronica sono un metodo speciale"


obj = MioOggetto(3)
print(type(obj))


class Calcolatrice:

    @staticmethod
    def somma(a, b):
        return a + b
    

risultato = Calcolatrice.somma(5, 3)
print(risultato)


class Contatore:
    numero_istanze = 0

    def __init__(self):
        Contatore.numero_istanze += 1
    
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
