# Funzione riutilizzabile (senza return)
def stampaSingola_lista(listaX:list):
    print("Benvenuto nella funzione")
    for i in listaX:
        print(i)
    print("Fine funzione")

lista = [*range(0,20,2)]

stampaSingola_lista(lista)

lista2 = [*range(1,20,2)]
stampaSingola_lista(lista2)

# Funzione con return
def ricalcoloValore(x:int):
    return x*7

numero = 10
numero = ricalcoloValore(numero)
print(numero)

def quadrato(numero:int):
    numero * numero

risultato = quadrato(4)
print(risultato)

