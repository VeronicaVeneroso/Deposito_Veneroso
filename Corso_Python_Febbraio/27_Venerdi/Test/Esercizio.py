import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generazione Dataset
orderID = np.random.choice(1000,500,replace=False) # Numero ordine generato random (non ripetibile)
customerID = np.random.choice(400,500,replace=True) # ID Cliente generato random (ripetibile)
elenco_prodotti = ["Telefono", "Tv", "Cuffie", "Computer",
            "Lavatrice", "Frigorifero", "Forno",
            "Reflex", "GoPro", "Drone"]
prodotti = np.random.choice(elenco_prodotti, size=500) # Lista prodotti generata dall'elenco precedente
prezzi = np.random.randint(100,2000, size=500) # Prezzi generati random tra 100 e 2000

# Generazione DataFrame con i dati generati precedentemente
df = pd.DataFrame({"Order ID" : orderID,
                   "Customer ID" : customerID,
                   "Prodotto" : prodotti,
                   "Prezzo" : prezzi})

# Sporco i dati
df.iloc[2] = df.iloc[0]
df.loc[3, "Prezzo"] = np.nan
df.loc[1, "Prodotto"] = np.nan

mapping_categoria = {
    "Telefono" : "Elettronica",
    "Tv" : "Elettronica",
    "Cuffie" : "Elettronica",
    "Computer" : "Elettronica",
    "Lavatrice" : "Elettrodomestico",
    "Frigorifero" : "Elettrodomestico",
    "Forno" : "Elettrodomestico",
    "Reflex" : "Fotografia",
    "GoPro" : "Fotografia",
    "Drone" : "Fotografia"
}

# Aggiungo colonna categoria in base al prodotto
df["Categoria"] = df["Prodotto"].map(mapping_categoria)
print(df.head(20)) # stampo le prime righe per controllare

# Riempio i prezzi vuoti con il valore medio
df["Prezzo"] = df["Prezzo"].fillna(df["Prezzo"].mean()).round(2)

# Tolgo righe con prodotto mancante
df = df.dropna(subset=["Prodotto"])
print(df.head(20)) # stampo le prime righe per controllare

# Stampo tabella con guadagno totale per categoria
df_categorie = df.groupby("Categoria")["Prezzo"].sum().reset_index()
df_categorie = df_categorie.rename(columns={"Prezzo": "Guadagno Totale"})
df_categorie = df_categorie.sort_values(by="Guadagno Totale",ascending=False)
print("\nGuadagno totale per categoria:\n", df_categorie)

# Stampo tabella con guadagno totale per prodotto
df_prodotti = df.groupby("Prodotto")["Prezzo"].sum().reset_index()
df_prodotti = df_prodotti.rename(columns={"Prezzo": "Guadagno Totale"})
df_prodotti = df_prodotti.sort_values(by="Guadagno Totale",ascending=False)
print("\nGuadagno totale per prodotto:\n", df_prodotti)

# Stampo tabella con vendita totale per cliente
df_clienti = df.groupby("Customer ID")["Prezzo"].sum().reset_index()
df_clienti = df_clienti.rename(columns={"Prezzo": "Spesa Totale"})
df_clienti = df_clienti.sort_values(by="Spesa Totale", ascending=False)
print("\nSpese totali per ogni cliente:\n", df_clienti.head(10))
cliente_top = df.groupby("Customer ID")["Prezzo"].sum().idxmax()
print("\nIl cliente che ha speso di più è il cliente ", cliente_top)

# Stampo categoria più venduta in termini di numero di prodotti venduti
categoria_piu_venduta = df["Categoria"].value_counts().idxmax()
print("\nLa categoria più venduta è stata: ", categoria_piu_venduta)

# Stampo prodotto più venduto in termini di numero
prodotto_piu_venduto = df["Prodotto"].value_counts().idxmax()
print("\nProdotto più venduto:", prodotto_piu_venduto)

# Plot di numero di prodotti venduti per categorie
conteggio_categorie = df["Categoria"].value_counts()

plt.figure()
plt.bar(conteggio_categorie.index, conteggio_categorie.values)
plt.title("Numero di vendite per categoria")
plt.xlabel("Categoria")
plt.ylabel("Numero di prodotti venduti per categoria")
plt.show()

# Plot di numero di prodotti venduti a confronto
conteggio_prodotti = df["Prodotto"].value_counts()

plt.figure()
plt.bar(conteggio_prodotti.index, conteggio_prodotti.values)
plt.title("Numero di vendite per prodotto")
plt.xlabel("Prodotto")
plt.ylabel("Numero di prodotti venduti")
plt.show()