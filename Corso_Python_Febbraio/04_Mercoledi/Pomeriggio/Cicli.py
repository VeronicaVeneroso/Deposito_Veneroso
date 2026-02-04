# ciclo while
conteggio = 0
while conteggio < 5:
    print(conteggio)
    conteggio += 1 # incremento di 1

count = 0
while count < 5:
    count += 1
    print(count)

# ciclo booleano
controllore = True
while controllore:
    print("oh no")
    esci = input("Vuoi uscire? SI - NO")
    if esci.lower() == "si":
        controllore = False
    else:
        controllore = True
# else -> condizione non necessaria ma utile
else:
    print("Ciclo while 1 - controllore era false")
print("Ciclo while terminato!")

# Ciclo for
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)

# stampa i numeri da 0 a 5 - 1 = 4
for i in range(5):
    print(i)

# stampa i numeri da 5 a 20 con passo di 3 alla volta
for c in range(5,21,3):
    print(c)

# ciclo for su stringa
stringa = "Veronica"
for l in stringa:
    print(l)