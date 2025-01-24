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
