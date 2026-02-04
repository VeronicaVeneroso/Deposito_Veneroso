# esercizi di stampa di variabili di vario tipo
nome = "Veronica"
eta = 32
print ("Mi chiamo ", nome, "e ho ", eta, " anni")

nome2 = input("Inserisci il tuo nome: ")
eta2 = int(input("Inserisci la tua età: "))
print("Ciao", nome2, "hai", eta2, "anni!")

sesso = ""
età = 0
sesso = input("Che sesso sei? ")
età = int(input("quanti anni hai? "))
print(sesso, età)


# esercizi operatori matematici
print(3+5)
print (4-2)
print(3*6)
print(8/2)
print(3**2) # potenza -> 3^2

x = 2
y = 3
print(x*y)

# esercizio concatenazione stringhe
a = "Ciao"
b = "Veronica"
print(a + " " + b)

# int: numero intero
num = 1

# float: numero decimale
num2 = 0.3

# differenza tra un intero e un decimale è decimale
x=1
y=0.2
z= x-y
print(z)

# Stampa della prima lettera di una stringa
a = input("Scrivi una parola: ")
print(a[0])

# Lunghezza di una stringa
x = input("Scrivi una parola: ")
print("La parola inserita ha lunghezza", len(x))

# Rendi tutta la stringa minuscolo
print(x.lower())

# Rendi tutta la stringa maiuscolo
print(x.upper())

# Separa una stringa
y = "Ciao Veronica"
print(y.split(' '))

# Sostituisce un elemento della stringa
print(y.replace("Veronica", "Mondo"))

# char
char = 'A'
print(char)

# variabili booleane
booleanT = True
booleanF = False
print(booleanT, booleanF)
# Trasformazione di booleano in intero
print(int(booleanF))
print(int(booleanT))

# Operatori di confronto con output booleano
x = 4
y = 5
print(x==y)
print(x!=y)
print(x<y)
print(x>y)