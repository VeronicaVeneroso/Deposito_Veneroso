'''Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà
di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti 1025 pokemon)'''

import random
import requests
import os
import json


def ottieni_pokemon_random():
    id_pokemon = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}/"


    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        
    except Exception as e:
        print(f"Errore di connessione: {e}")
    return None

    
def ottieni_specifiche_pokemon(pokemon):

    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"

    res = requests.get(url)

    return res.json()['capture_rate']

def mostra_pokemon(RISS: dict):
    if RISS:

        nome = RISS['name'].upper()
        identificativo = RISS['id']
        altezza = RISS['height']
        peso = RISS['weight']
        # sesso = RISS['gender']

        tipi = ", ".join([t['type']['name'] for t in RISS['types']])

        print("-" * 30)
        print(f"POKEMON TROVATO!")
        print(f"Nome:    {nome}")
        print(f"ID:      #{identificativo}")
        print(f"Tipo/i:  {tipi}")
        # print(f"Sesso: {sesso}")
        print(f"Altezza: {altezza}")
        print(f"Peso:    {peso}")
        catch_rate = ottieni_specifiche_pokemon(identificativo)
        print(f"cath rate",catch_rate)
        print("-" * 30)
        
        return catch_rate, nome, identificativo
    else:
        print("Non è stato possibile trovare nessun Pokemon.")
        
def Cattura(catch_rate):

    lancio = random.randint(1,225)
    print(f"lancio:  {lancio}")

    return lancio <= catch_rate


mio_pokedex = {
    "CHARIZARD" : f"https://pokeapi.co/api/v2/pokemon-species/{"0006"}"
}

squadra = {
    "CHARIZARD" : f"https://pokeapi.co/api/v2/pokemon-species/{"0006"}"
}

def play(squadra: dict):
        
    print("entri nelle'erba alta")
    random_pokemon = ottieni_pokemon_random()
    random_pokemon = mostra_pokemon(random_pokemon)
    
    nome_primo_pokemon = list(squadra.keys())[0]
    print(f"\n mandi in campo {nome_primo_pokemon}")
    
    
    presente = None
    if not random_pokemon[1] in mio_pokedex:
        print("non presente nel tuo pokedex!")
        presente = False
        

    while True:  
        scelta = input("cosa vuoi fare? :\n 1)scappa\n 2)cattura : ").lower()
        if not scelta in ("1", "2") :
            break
        
        else:
            if scelta == "1":
                print("ciao!")
                break
            
            if scelta == "2": 
                print("\nlancia la ball")
                if Cattura(random_pokemon[0]):

                    print("cattura completata!\n")
                    # metti_in_squadra(random_pokemon)
                    if presente == False:
                        mio_pokedex[str(random_pokemon[1])] = f"https://pokeapi.co/api/v2/pokemon-species/{random_pokemon[2]}"
                        print("pokedex attuale: ", mio_pokedex)
                        if len(squadra) < 6 :
                            squadra[str(random_pokemon[1])] = f"https://pokeapi.co/api/v2/pokemon-species/{random_pokemon[2]}"
                            print(random_pokemon[1], "\naggiunnto in sqiuadra!")
                        else:
                            print(random_pokemon[1], "\naggiunnto in pc!")
                        print("squadra attuale: ", squadra)
                    break
                else:
                    print("e uscito dalla ball!")
            else:
                print("uscita!")
                break
    
        
play(squadra)



# def metti_in_squadra (random_pokemon):
#     nome_file = "/Users/marcoaureliodefelicis/Documents/GitHub/progetti python/Senza nome/progetto_di_gruppo_py_GliBOH/squadra.json"
#     nome_pokemon = random_pokemon[1]
#     contenuto_pokemon = f"https://pokeapi.co/api/v2/pokemon-species/{random_pokemon[2]}"
    
#     if os.path.exists(nome_file):
#         with open(nome_file, "r") as file:
#             try:
#                 lista = json.load(file)
#             except:
#                 lista = []
#     else:
#         lista = [] 
    
#     lista.append(nome_pokemon, contenuto_pokemon)
    
#     if not nome_pokemon in file: 

#         with open(nome_file, "w") as file:
#             json.dump(lista, file, indent=4)
    
#         return f"Ottimo lavoro! {nome_pokemon} è ora nel file JSON."