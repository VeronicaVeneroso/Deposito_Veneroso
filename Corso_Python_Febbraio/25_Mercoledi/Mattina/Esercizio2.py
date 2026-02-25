import pandas as pd

'''Esercizio 2: Manipolazione e Aggregazione dei Dati
Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
1.Caricare i dati in un DataFrame.
2.Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
3.Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
4.Trovare il prodotto più venduto in termini di Quantità.
5.Identificare la città con il maggior volume di vendite totali.
6.Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
7.Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
8.Visualizzare il numero di vendite per ogni città.'''

# Creazione dati casuali
data = {
    "Prodotto": ["Computer", "Smartphone", "Tastiera", "Mouse", "Cuffie", "Computer"],
    "Quantità": [10, 22,50,40,3,45],
    "Prezzo unitario": [800, 400, 100, 50, 40, 800],
    "Città": ["Roma", "Milano", "Napoli", "Napoli", "Milano", "Roma"]
}

df = pd.DataFrame(data)
print("\nDataFrame originale:\n", df)

df["Totale Vendite"] = df["Quantità"] * df["Prezzo unitario"]
print("\nDataFrame con Totale Vendite:\n", df)

vendite_per_prodotto = df.groupby("Prodotto", as_index=False)["Totale Vendite"].sum()
print("\nDataFrame con prodotti raggruppati:\n", vendite_per_prodotto)

quantita_per_prodotto = df.groupby("Prodotto")["Quantità"].sum().reset_index()
print("\nQuantità di prodotti venduti:\n", quantita_per_prodotto)
id_max = quantita_per_prodotto["Quantità"].idxmax()
piu_venduto = quantita_per_prodotto.loc[id_max,"Prodotto"]
print("\nIl prodotto più venduto è: ", piu_venduto)

vendite_per_città = df.groupby("Città")["Quantità"].sum().reset_index()
print("\nNumero di prodotti venduti per ogni città:\n", vendite_per_città)
id_max = vendite_per_città["Quantità"].idxmax()
citta = vendite_per_città.loc[id_max,"Città"]
print("\nLa città che ha venduto più prodotti è: ", citta)

vendite_maggiori = df[df["Totale Vendite"] > 1000]
print("\nVendite superiori a 1000€:\n", vendite_maggiori)