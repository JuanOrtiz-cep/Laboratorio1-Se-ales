import wfdb
import matplotlib.pyplot as mp
import numpy as np
record = wfdb.rdrecord('cu01')

print("Información del registro")
print(record.__dict__)
original_signal = record.p_signal[:,0] #asumiendo que es un canal único
fs = record.fs #frecuencia de muestreo
num_muestras_10s = fs*10
time_10s = np.arange(num_muestras_10s)/fs #solo se toman los 10 primeros segundos
#time = np.arange(len(signal))/fs  #eje de tiempo

mp.figure(figsize=(12,4))
mp.plot(time_10s, original_signal[:num_muestras_10s], label='señal original')
mp.grid()
mp.title('señal fisiologica (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')

mp.show()

#Edicion 27/01/25

#VALORES DADOS CON EL USO DE LAS BIBLIOTECAS (NUMPY)

#mean_signal = np.mean(signal)
#std_signal = np.std(signal)
#cv_signal = std_signal / mean_signal

#VALORES SIN EL USO DE NUMPY

n = len(original_signal)
sum_signal = 0
for x in original_signal:
    sum_signal += x
mean_signal = sum_signal / n
suma_cuadrados_diferencias = 0
for x in original_signal:
    suma_cuadrados_diferencias +=(x-mean_signal)**2

varianza = suma_cuadrados_diferencias / (n-1)
std_signal = varianza**0.5
cv_signal = std_signal / mean_signal

print(f"Media: {mean_signal}")
print(f"Desviación estándar: {std_signal}")
print(f"Coeficiente de variación: {cv_signal}")

# Histograma
mp.figure(figsize=(8, 5))
mp.hist(original_signal, bins=20, alpha=0.7, color='blue', edgecolor='black')
mp.title('Histograma de la señal')
mp.xlabel('Valor de la señal')
mp.ylabel('Frecuencia')
mp.grid()
mp.show()

# FUNCION DE PROBABILIDAD CON NUMPY
#counts, bins = np.histogram(original_signal, bins=20) # Ajusta el número de bins según sea necesario

# FUNCION DE PROBABILIDAD SIN NUMPY
min_val = min(original_signal)
max_val = max(time_10s)
num_bins = 100
bin_width = (max_val - min_val) / num_bins
counts = [0] * num_bins

for value in original_signal:
    bin_index = int((value - min_val) / bin_width)
    counts[bin_index] += 1

# Normaliza el histograma
probabilidad = [count / len(original_signal) for count in counts]

# Crea los bins para el gráfico
bins = [min_val + i * bin_width for i in range(num_bins + 1)]

# Grafica la función de probabilidad

mp.plot(bins[:-1], probabilidad)
mp.xlabel('Amplitud de la señal')
mp.ylabel('Probabilidad')
mp.title('Función de probabilidad de la señal fisiológica')
mp.grid()
mp.show()

#RUIDO GAUSSIANO

# Parámetros distribución gaussiana
media = 0      # Media de la distribución (el centro de la campana)
desviacion_estandar = 0.1  # Desviación estándar (el ancho de la campana)
longitud = len(original_signal)  # Longitud del array de ruido
gaussian_noise = np.random.normal(media, desviacion_estandar, longitud)

gaussian_signal= original_signal + gaussian_noise

mp.figure(figsize=(12,4))
mp.plot(time_10s, gaussian_signal[:num_muestras_10s], label='señal ruido gaussiano')
mp.grid()
mp.title('señal ruido gaussiano (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_gausiano = np.mean(gaussian_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_gausiano)
print(f"SNR Gauss: {snr} dB")


#ruido gaussiano 2

# Parámetros distribución gaussiana
media = 0      # Media de la distribución (el centro de la campana)
desviacion_estandar = 0.2 # Desviación estándar (el ancho de la campana)
longitud = len(original_signal)  # Longitud del array de ruido
gaussian_noise = np.random.normal(media, desviacion_estandar, longitud)

gaussian_signal= original_signal + gaussian_noise

mp.figure(figsize=(12,4))
mp.plot(time_10s, gaussian_signal[:num_muestras_10s], label='señal ruido gaussiano')
mp.grid()
mp.title('señal ruido gaussiano 2 (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_gausiano = np.mean(gaussian_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_gausiano)
print(f"SNR Gauss 2: {snr} dB")


#RUIDO IMPULSO

num_impulses = 100  # Número de impulsos
impulse_amplitude = 5  # Amplitud de los impulsos
impulse_noise = np.zeros(len(original_signal))# se crea un arreglo de ceros del tamaño de la señal original

impulse_positions = np.random.choice(len(original_signal), num_impulses, replace=False) #crear impulsos aleatorios
impulse_noise[impulse_positions] = impulse_amplitude

impulse_signal = original_signal + impulse_noise

mp.figure(figsize=(12,4))
mp.plot(time_10s, impulse_signal[:num_muestras_10s], label='señal ruido impulso')
mp.grid()
mp.title('señal ruido impulso (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_impulso = np.mean(impulse_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_impulso)
print(f"SNR Impulso: {snr} dB")

#ruido impulso 2
num_impulses = 100  # Número de impulsos
impulse_amplitude = 10  # Amplitud de los impulsos
impulse_noise = np.zeros(len(original_signal))# se crea un arreglo de ceros del tamaño de la señal original

impulse_positions = np.random.choice(len(original_signal), num_impulses, replace=False) #crear impulsos aleatorios
impulse_noise[impulse_positions] = impulse_amplitude

impulse_signal = original_signal + impulse_noise

mp.figure(figsize=(12,4))
mp.plot(time_10s, impulse_signal[:num_muestras_10s], label='señal ruido impulso 2')
mp.grid()
mp.title('señal ruido impulso 2 (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_impulso = np.mean(impulse_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_impulso)
print(f"SNR Impulso 2: {snr} dB")



#RUIDO ARTEFACTO

#Interferencia linea electrica (60 Hz)
i_frequency = 60
i_amplitude = 0.1


#device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * time_10s)
device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * np.arange(len(original_signal)) / fs)
#device_noise = len(original_signal)
device_signal = original_signal + device_noise


mp.figure(figsize=(12,4))
mp.plot(time_10s, device_signal[:num_muestras_10s], label='señal ruido aparato')
mp.grid()
mp.title('señal ruido artefacto (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_artefacto = np.mean(device_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_artefacto)
print(f"SNR Artefacto: {snr} dB")


#ruido artefacto 2


#Interferencia linea electrica (60 Hz)
i_frequency = 60
i_amplitude = 0.5


#device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * time_10s)
device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * np.arange(len(original_signal)) / fs)
#device_noise = len(original_signal)
device_signal = original_signal + device_noise


mp.figure(figsize=(12,4))
mp.plot(time_10s, device_signal[:num_muestras_10s], label='señal ruido artefacto')
mp.grid()
mp.title('señal ruido artefacto (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()

cuadrado_osignal = np.mean(original_signal**2)
cuadrado_ruido_artefacto = np.mean(device_noise**2)

# Calcula el SNR en decibeles (dB)
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_artefacto)
print(f"SNR Artefacto: {snr} dB")
