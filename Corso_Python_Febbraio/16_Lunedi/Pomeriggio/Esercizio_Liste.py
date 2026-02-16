''' Scrivi un programma che chiede all'utente una serie di parole
e restituisce solo le vocali e l'indice della vocale all'interno delle parole'''

lista_parole = input("Inserisci varie parole separate da spazio: ").lower().split()
vocali = ["a", "e", "i", "o", "u"]

for parola in lista_parole:
    index = 0
    print(f"Parola {parola}")
    for lettera in parola:
        if lettera in vocali:
            print(f"{lettera}, {index}")
        index += 1
