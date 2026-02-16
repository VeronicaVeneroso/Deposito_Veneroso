'''Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10'''

lista_alunni = {}
while True:
    nome = input("Inserisci nome studente oppure scrivi \"media\" se vuoi visualizzare la media di ogni studente: ")
    if nome.lower() == "media":
        for alunno in lista_alunni:
            voti = lista_alunni[alunno]
            if len(voti) > 0:
                media = sum(voti)/len(voti)
                print(f"L'alunno {alunno} ha media {media}")
            else:
                print(f"Per l'alunno {alunno} non ci sono voti inseriti.")
        break
    voti = []
    while True:
        voto = input(f"Inserisci nuovo voto per {nome} oppure scrivi \"stop\" per passare all'alunno successivo o alle medie: ")
        if voto.lower() == "stop":
            break
        else:
            voti.append(float(voto))
    lista_alunni[nome] = voti