'''Esercizio 1: Analisi di Vendite Fittizie
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data","Città","Prodotto" e "Vendite".
I dati devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.
1.Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.
2.Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
3.Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto.'''

import pandas as pd
import numpy as np

date = pd.date_range(start="2026-01-01", end="2026-01-31")
citta = ["Milano", "Napoli", "Roma"]
prodotti = ["Smartphone", "Tv", "Computer"]

data = {
    "Data" : np.random.choice(date,20),
    "Città" : np.random.choice(citta,20),
    "Prodotto" : np.random.choice(prodotti,20),
    "Vendite" : np.random.randint(0,1000,20)
}

df = pd.DataFrame(data)
print("\nDATAFRAME ORIGINALE:\n", df)

pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("\nVENDITE MEDIE PRODOTTO PER CITTA':\n", pivot_df)

grouped_df = df.groupby('Prodotto')["Vendite"].sum().reset_index()
print("\nVENDITE TOTALI PER PRODOTTO:\n", grouped_df)