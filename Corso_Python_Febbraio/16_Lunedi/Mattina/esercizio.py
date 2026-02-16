'''create un programma che richiede all’utente tre numeri e verifica la presenza
di almeno due numeri uguali, se non ci sono ci restituisce il numero più grande dei tre'''

print("Inserisci 3 numeri")
num1 = int(input("primo numero: "))
num2 = int(input("secondo numero: "))
num3 = int(input("terzo numero: "))

if num1 == num2 or num1 == num3 or num2 == num3: print("Ci sono due numeri uguali")
elif num1 > num2 and num1> num3: print(f"Il numero più grande è {num1}")
elif num2 > num3: print(f"Il numero più grande è {num2}")
else: print(f"Il numero più grande è {num3}")