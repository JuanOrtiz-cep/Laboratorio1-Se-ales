import wfdb
import matplotlib.pyplot as mp
import numpy as np
record = wfdb.rdrecord('cu01')

print("Información del registro")
print(record.__dict__)
signal = record.p_signal[:,0] #asumiendo que es un canal único
fs = record.fs #frecuencia de muestreo
num_muestras_10s = fs*10
time_10s = np.arange(num_muestras_10s)/fs
#time = np.arange(len(signal))/fs  #eje de tiempo

mp.figure(figsize=(12,4))
mp.plot(time_10s, signal[:num_muestras_10s], label='señal original')
mp.title('señal fisiologica (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud')
mp.legend()
mp.grid()
mp.show()

#Edicion 27/01/25

#mean_signal = np.mean(signal)
#std_signal = np.std(signal)
#cv_signal = std_signal / mean_signal

n = len(signal)
mean_signal = sum(signal) / n
suma_cuadrados_diferencias = sum((x-mean_signal)**2 for x in signal)
varianza = suma_cuadrados_diferencias / (n-1)
std_signal = varianza**0.5
cv_signal = std_signal / mean_signal * 100

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
