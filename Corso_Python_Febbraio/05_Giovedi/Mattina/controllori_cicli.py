numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    if numero == 3:
        break # ferma il ciclo
    print(numero)

for numero in numeri:
    if numero == 3:
        continue # salta un giro
    print(numero)

if True:
    # qui andrà il menu dell'utente
    # serve solo a dire che ci sarà un pezzo di codice prima o poi
    pass


# operatore splat: espande la sequenza di numeri del range in una lista
# al posto di range si può mettere un database specificando magari la riga
numeri = [*range(1, 11)]
print(numeri)