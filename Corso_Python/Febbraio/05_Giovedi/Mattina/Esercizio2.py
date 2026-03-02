# Numeri primi in un intervallo : 
# Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e
# 50). Il programma dovrebbe stampare tutti i numeri primi compresi in
# quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in
# due aggregazioni differenti e chiedere se deve ripetere
risposta = "si"

while risposta == "si":
    # Inizializzazione liste
    numeri_primi = []
    numeri_non_primi = []
    # Inserimento di inzio e fine intervallo
    start = int(input("Inserisci il numero intero di inizio intervallo: "))
    stop = int(input("Inserisci il numero intero di fine intervallo: "))
    
    # per ogni numero dell'intervallo controlla se è primo o non lo è
    for numero in range(start, stop, 1):
        if numero < 2:
            numeri_non_primi.append(numero)
        else:
            primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

            if primo:
                numeri_primi.append(numero)
            else:
                numeri_non_primi.append(numero)
    
    # Richiede all'utente se stampare i numeri primi, i non primi o entrambi
    print("Opzioni disponibili:\n1 - Stampare solo elenco numeri primi\n2 - Stampare solo elenco numeri non primi\n3 - Stampare entrambi gli elenchi")
    scelta = input("Scegli quale elenco stampare: ")
    match scelta:
        case "1":
            print("Elenco di numeri primi: ", numeri_primi)
        case "2":
            print("Elenco di numeri non primi: ", numeri_non_primi)
        case "3":
            print("Elenco di numeri primi: ", numeri_primi)
            print("Elenco di numeri non primi: ", numeri_non_primi)
        case _:
            print("Opzione selezionata non valida")
    
    # Richiesta di ripetere
    risposta = input("Vuoi ripetere tutto il procedimento? (si/no)").lower()
