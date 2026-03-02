import numpy as np

A = np.array([[1,2],[3,4]])

A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)

v = np.array([3,4])
# Norma 1 (Somma valori assoluti degli elementi)
norm_v = np.linalg.norm(v)
print("Norma di v: ", norm_v)

C = np.array([[3,1],[1,2]])
B = np.array([9,8])
# Risoluzione sistema lineare Cx=B
x = np.linalg.solve(C,B)
print("Soluzione x: ", x)

# Trasformata di Fourier:
# Creazione di un segnale
t = np.linspace(0,1,400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della trasformata
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier: ", fft_sig)
print("Frequenze associate: ", freqs)

# Broadcasting
arr = np.array([1,2,3,4])
scalar = 10

result = arr + scalar
print(result)