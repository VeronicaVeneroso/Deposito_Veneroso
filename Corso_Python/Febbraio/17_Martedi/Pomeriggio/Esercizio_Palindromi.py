'''Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma'''

def palindromo(frase:str):
    new_frase = frase.lower()

    for carattere in frase.lower():

        if not carattere.isalpha():
            new_frase = new_frase.replace(carattere,"")

    frase_invertita = new_frase[::-1]
    
    if new_frase == frase_invertita:
        print(f"La frase {frase} è palindroma")
    else:
        print(f"La frase {frase} non è palindroma")


frase = input("Inserisci una frase: ")
palindromo(frase)