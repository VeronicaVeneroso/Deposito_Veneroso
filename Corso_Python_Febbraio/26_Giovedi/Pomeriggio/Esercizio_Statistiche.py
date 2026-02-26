'''Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese.
Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:
La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lista_giorni = pd.date_range(start="2026-01-01", end="2026-01-31", freq="D")
giorni = np.repeat(lista_giorni, 24)
ore = np.tile(range(0,24), 31)
temperature = np.random.uniform(0,30,24*31).round(1)

df = pd.DataFrame({"Giorno" : giorni, "Ora" : ore, "Temperatura": temperature})

print("\nTemperature di gennaio:\n", df.head(31))

statistiche = df.groupby("Giorno")["Temperatura"].agg(Temperatura_Massima = "max",
                                                          Temperatura_Minima = "min",
                                                          Temperatura_Media="mean",
                                                          Temperatura_Mediana = "median")
statistiche["Temperatura_Media"] = statistiche["Temperatura_Media"].round(2)
print("\nStatistiche giornaliere:\n", statistiche)

plt.figure()
plt.plot(statistiche.index, statistiche["Temperatura_Massima"],color="red", label="Temperatura Massima")
plt.plot(statistiche.index, statistiche["Temperatura_Minima"], color="blue", label="Temperatura Minima")
plt.title("Temperature massime e minime giornaliere")
plt.xlabel("Giorni")
plt.ylabel("Temperature")
plt.legend()
plt.show()

plt.figure()
plt.plot(statistiche.index, statistiche["Temperatura_Media"],color="red", label="Temperatura Media")
plt.plot(statistiche.index, statistiche["Temperatura_Mediana"], color="blue", label="Temperatura Mediana")
plt.title("Temperature medie e mediane giornaliere")
plt.xlabel("Giorni")
plt.ylabel("Temperature")
plt.legend()
plt.show()