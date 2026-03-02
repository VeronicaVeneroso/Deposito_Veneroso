'''Scrivete un programma che chiede una stringa all’utente e restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio: Stringa "ababcc", Risultato {"a": 2, "b": 2, "c": 2}'''

stringa = input("Inserisci un testo: ")
frequenza_lettere = {}
for lettera in stringa.lower():
    if lettera in frequenza_lettere:
        frequenza_lettere[lettera] += 1
    else:
        frequenza_lettere[lettera] = 1

print(frequenza_lettere)