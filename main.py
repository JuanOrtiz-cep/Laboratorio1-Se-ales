import wfdb
import matplotlib.pyplot as mp
import numpy as np
record = wfdb.rdrecord('cu01')

print("Información del registro")
print(record.__dict__)
signal = record.p_signal[:,0] #asumiendo que es un canal único
fs = record.fs #frecuencia de muestreo
time = np.arange(len(signal))/fs  #eje de tiempo

mp.figure(figsize=(12,4))
mp.plot(time, signal, label='señal original')
mp.title('señal fisiologica (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud')
mp.legend()
mp.grid()
mp.show()
#Edicion 27/01/25

mean_signal = np.mean(signal)
std_signal = np.std(signal)
cv_signal = std_signal / mean_signal

print(f"Media: {mean_signal}")
print(f"Desviación estándar: {std_signal}")
print(f"Coeficiente de variación: {cv_signal}")

# Histograma
mp.figure(figsize=(8, 5))
mp.hist(signal, bins=20, alpha=0.7, color='blue', edgecolor='black')
mp.title('Histograma de la señal')
mp.xlabel('Valor de la señal')
mp.ylabel('Frecuencia')
mp.grid()
mp.show()
