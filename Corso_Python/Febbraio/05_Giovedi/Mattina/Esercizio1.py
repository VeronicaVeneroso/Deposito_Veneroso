# Numeri pari e dispari o sequenza Descrizione: 
# Scrivi un programma che chiede all'utente di inserire un numero o una stringa
# scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o
# dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.

# Stringa o numero?
# Se è numero stampa se è pari o dispari
# Se è stringa stampa se il numero di caratteri è pari o dispari
# Vuoi ripetere con lo stesso tipo di dato? Vuoi cambiare dato? Vuoi smettere?

risposta = "si"

while risposta == "si":
    scelta = input("Vuoi inserire una stringa o un numero? (stringa/numero) ").lower()
    
    if scelta == "stringa":
        valore = input("Inserisci la tua stringa: ")
        numero = len(valore)
        if numero % 2 == 0:
            print("La lunghezza della parola è", numero, "ed è un numero pari")
        else:
            print("La lunghezza della parola è", numero, "ed è un numero dispari")

    elif scelta == "numero":
            valore = int(input("Inserisci il tuo numero: "))
            numero = valore
            if numero % 2 == 0:
                print("Il numero scelto è", numero, "ed è un numero pari")
            else:
                print("Il numero scelto è", numero, "ed è un numero dispari")

    else:
        print("L'opzione selezionata non è valida")

    risposta = input("Vuoi ripetere il procedimento? (si/no)").lower()