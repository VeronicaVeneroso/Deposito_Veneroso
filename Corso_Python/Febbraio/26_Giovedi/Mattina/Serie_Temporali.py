import pandas as pd
import numpy as np

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='ME')
df = pd.DataFrame({'value': np.random.randint(1, 100, size=10)}, index=date_range)
# Resampling dei dati di una serie temporale
df_resampled = df.resample('ME').mean()

# esempio: colonna "date" in stringhe -> datetime
df['date'] = pd.to_datetime(date_range['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(date_range['date'])

# partendo da un DataFrame con indice DatetimeIndex
df_daily = df.resample('D').mean() # media giornaliera
df_monthly = df.resample('ME').sum() # somma mensile

# aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)
# tasso di variazione giornaliero
df['daily_return'] = df ['value'].pct_change()
# equivalente a shift + calcolo %

# finestra mobile di 7 giorni: media e deviazione standard
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7'] = df['value'].rolling(window=7).std()
