'''1. Definisca una funzione chiamata conta_vocali. 
2. La funzione deve: 
- ricevere una stringa come parametro 
- contare quante vocali contiene (a, e, i, o, u) 
- restituire il numero totale di vocali 
3. Nel programma principale: 
- chiedi all’utente di inserire una parola 
- chiama la funzione 
- stampa il numero di vocali trovate'''

# Funzione che conta le vocali di una parola
def conta_vocali(parola):
    # Inizializza il numero di vocali a 0
    vocali = 0
    # Ad ogni ciclo incrementa la variabile vocali solo se la lettera è una vocale
    for i in parola:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vocali = vocali + 1
    return(vocali)

# Chiede in input una parola all'utente
scelta = input("Inserisci una parola a tua scelta: ")
# Richiama la funzione per contare le vocali della parola scelta
numero_vocali = conta_vocali(scelta)
# Stampa il numero di vocali della parola
print(numero_vocali)
