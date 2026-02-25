import pandas as pd
import random
import numpy as np

'''Utilizzare  un dataset di esempio che include le seguenti informazioni
su un gruppo di persone: Nome, Età, Città e Salario.

1. Caricare i dati in un DataFrame autogenerandoli casualmente.
2. Visualizzare le prime e le ultime cinque righe del DataFrame.
3. Visualizzare il tipo di dati di ciascuna colonna.
4. Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard)
5. Identificare e rimuovere eventuali duplicati
6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.
7. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone
come "Giovane", "Adulto" o "Senior" basandosi sull'età (0-18 / 19-65 / >65)
8. Salvare il DataFrame pulito in un nuovo file CSV.'''

def categoria_eta(eta):
    if eta < 18:
        return "Giovane"
    elif eta < 65:
        return "Adulto"
    else:
        return "Senior"

nomi = [
    "Luca", "Marco", "Giulia", "Anna", "Paolo", "Sara",
    "Francesca", "Davide", "Chiara", "Alessandro",
    "Martina", "Simone", "Elena", "Giorgio", "Valentina",
    "Roberto", "Federica", "Andrea", "Laura", "Stefano",
    "Marta", "Fabio", "Silvia", "Antonio", "Ilaria"
]

citta = ["Roma", "Milano", "Napoli", "Torino", "Bologna", "Firenze"]

# Creazione dati casuali
data = {
    "Nome": random.sample(nomi, 20),
    "Età": np.random.randint(0, 100, 20),
    "Città": np.random.choice(citta, 20),
    "Salario": np.random.randint(1000, 10000, 20)
}

df = pd.DataFrame(data)
df.loc[3, "Età"] = np.nan
df.loc[5, "Salario"] = np.nan

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("\nDataFrame completo:\n", df)

print("\nLe prime righe sono:\n", df.head())
print("\nLe ultime righe sono:\n", df.tail())

print("\nTipi di dati per colonna:")
print(df.dtypes)

print("\nStatistiche descrittive:")
print("\nEtà media: ", df['Età'].mean())
print("Salario medio: ", df['Salario'].mean())

print("\nMediane:\n", df.median(numeric_only=True).to_string())
print("\nDeviazioni Standard:\n", df.std(numeric_only=True).to_string())

df[df.duplicated()]
df.drop_duplicates()

df['Età'].fillna(df['Età'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)

df['Categoria Età'] = df['Età'].apply(categoria_eta)

print("\nDataset finale:")
print(df)

df.to_csv("dataset_pulito.csv", index=False)