'''Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà
di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti 1025 pokemon)'''

import requests

# URL dell'endpoint PokéAPI
url = "https://pokeapi.co/api/v2/pokemon?limit=1"

# Facciamo la richiesta GET
response = requests.get(url)

# Convertiamo la risposta in formato JSON
data = response.json()

# Stampiamo il numero totale di Pokémon
print("Numero totale di Pokémon salvati nella PokéAPI:", data["count"])