# Laboratorio 1 Señales

# **NOTA:** El codigo se completo se encuentra en el lab1main.py

# Visualizador de Señales Electrocardiográficas (ECG)

Este repositorio contiene un script de Python simple para cargar y visualizar señales electrocardiográficas (ECG) a partir de archivos .hea y .dat de PhysioNet.
## Objetivos
 * Descargar y visualizar una señal fisiológica.
 
 * Calcular estadísticos descriptivos (media, desviación estándar, coeficiente de variación, histogramas, función de probabilidad).
 
 * Introducir ruido (gaussiano, impulsivo y de aparato) y calcular la relación señal-ruido (SNR).
  
## Requisitos
* **Python:** Se requiere una instalación de Python 3.x.
* **Bibliotecas:**
  * `wfdb`: Para leer archivos de PhysioNet.
  * `matplotlib`: Para crear gráficos.
  * `numpy`: Para realizar operaciones numéricas.

  * **Archivos physionet**

## PROCEDIMIENTO
# *1. Instalacion librerias*
    
  ```bash
 pip install wfdb numpy matplotlib (abrir CMD para instalar esas librerias o directamente en la terminal )
```

Crear un archivo con las siguientes líneas (Python) :

```python
import wfdb as wf  
import numpy as np # El as es utilizado para renombrar a la libreria y poder llamarla mas facil
import matplotlib.pyplot as mp
```
  
* wfdb: para la lectura de la señal de PhysioNet
* matplotlib: para la graficación
* numpy: para los datos estadisticos

# *2. Usando la web physionet descarga un archivo de ECG:*

Coloca el archivo .hea y .dat (por ejemplo, cu01.hea, cu01.dat) en la misma carpeta que el script de Python.
esto para que se lean correctamente los archivos:

```python
record = wfdb.rdrecord('cu01') #LECTURA DEL ARCHIVO ECG

print("Información del registro")
print(record.__dict__)
signal = record.p_signal[:,0] #asumiendo que es un canal único ,seleccionar un canal diferente si el registro tiene múltiples canales
fs = record.fs #frecuencia de muestreo
num_muestras_10s = fs*10
time_10s = np.arange(num_muestras_10s)/fs ##10 SEGUNDOS del muestreo de datos
```

 
# *3. Personalización del gráfico (matplotlib).*
   
   ```python
   
   mp.figure(figsize=(12, 4))
   mp.plot(time, signal, label='Señal original')
   mp.title('Señal Fisiológica (cu01)')
   mp.xlabel('Tiempo (s)')
   mp.ylabel('Voltaje(mv)')
   mp.legend()
   mp.grid()
   ```

![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Se%C3%B1alFisiologica(original).jpeg)



# *4. Datos estadisticos y Histograma*
   
La explicacion de cada linea de codigo se encuentra en los comentarios de la parte del codigo
 ```python
  n = len(original_signal)  # Cantidad de datos en la señal
sum_signal = 0  # Inicializamos la suma en 0

for x in original_signal:
    sum_signal += x  # Sumamos cada valor de la señal

mean_signal = sum_signal / n  # Calculamos la media (promedio)

suma_cuadrados_diferencias = 0
for x in original_signal:
    suma_cuadrados_diferencias += (x - mean_signal) ** 2  # Calculamos la diferencia de cada valor con la media

varianza = suma_cuadrados_diferencias / (n - 1)  # Calculamos la varianza
std_signal = varianza ** 0.5  # La desviación estándar es la raíz cuadrada de la varianza
cv_signal = std_signal / mean_signal  # El coeficiente de variación mide cuánta variabilidad hay respecto a la media

Media: -0.22333603181589465
Desviación estándar: 0.44077231632548347
Coeficiente de variación: -1.973583540200225

```


* Media: El promedio de los valores en la señal.
* Varianza: Nos dice qué tan dispersos están los datos respecto a la media.
* Desviación estándar: Es la raíz cuadrada de la varianza y nos dice cuánto varían los valores en promedio.
* Coeficiente de Variación (CV): Mide la variabilidad relativa respecto a la media.

### **Una vez realizado los calculos estadisticos , se crea una interfaz para el histograma con las funciones de matplotlib similares al punto 3**

![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/155112a9-58bf-45c5-82b3-6cde9e2dfb59.jpg)
   

# *5. Funcion de probabilidad*

Este código toma los valores de la señal, los agrupa en 100 categorías y calcula cuántas veces aparece cada valor dentro de esos grupos. Luego, normaliza estos valores para obtener la probabilidad de ocurrencia de cada grupo y genera los límites de cada bin para graficar la función de probabilidad.


**La siguiente parte del codigo toma los valores de la señal y los organiza en 100 grupos para calcular la probabilidad de ocurrencia de cada valor. A continuación, explicamos cada línea del código.**


**Se obtiene el valor mínimo de la señal, que será el límite inferior del rango en el que se agruparán los valores.**

```python
min_val = min(original_signal)  # Encuentra el valor más pequeño en la señal
```

**Se encuentra el valor máximo de la señal, que será el límite superior del rango.**

```python
max_val = max(original_signal)  # Encuentra el valor más grande en la señal
```

**Aquí definimos 100 grupos (bins) para organizar los valores de la señal dentro de un rango.**

```python
num_bins = 100  # Número de divisiones o grupos en los que se agruparán los valores
```

**El tamaño de cada grupo se obtiene dividiendo el rango de valores entre la cantidad de grupos.**

```python
bin_width = (max_val - min_val) / num_bins  # Calcula el tamaño de cada grupo
```

**Se inicializa una lista con 100 posiciones en cero, donde se contarán los valores de la señal que caen en cada grupo.**

```python
counts = [0] * num_bins  # Crea una lista con 100 espacios inicializados en 0
```
**Se recorre cada valor de la señal y se calcula a qué grupo pertenece. Luego, se suma 1 en ese grupo para contar cuántos valores caen en él.**

```python
for value in original_signal:
    bin_index = int((value - min_val) / bin_width)  # Encuentra en qué grupo cae el valor
    counts[bin_index] += 1  # Aumenta el contador en ese grupo
```
**Los conteos se dividen entre la cantidad total de datos para convertirlos en probabilidades, asegurando que la suma total sea 1.**

```python
probabilidad = [count / len(original_signal) for count in counts]
```

**Se genera una lista con los límites de cada bin para poder graficar correctamente los resultados.**
```python
bins = [min_val + i * bin_width for i in range(num_bins + 1)]  # Crea los límites de cada grupo
```
 ![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Funcion%20probabilidad.jpg)

 # *6. Ruidos en las señales*

## *6.1 Ruidos gausianos*
Se define un ruido gaussiano con:

Media = 0 → El ruido está centrado en cero.

Desviación estándar = 0.1 → La amplitud del ruido varía en un rango pequeño.

Longitud = len(original_signal) → Se genera un ruido de la misma longitud que la señal original.

np .random : genera una señal aleatoria con distribución normal, es decir, una secuencia de valores que siguen una campana de Gauss.

 ## *Para el ruido gaussiano 1*
```python
media = 0      # Media de la distribución (el centro de la campana)
desviacion_estandar = 0.1  # Desviación estándar (el ancho de la campana)
longitud = len(original_signal)  # Longitud del array de ruido
gaussian_noise = np.random.normal(media, desviacion_estandar, longitud)
```


*Suma de la señal original con el ruido*

* Esto da como resultado una señal ruidosa, donde la forma original de la señal sigue presente, pero con pequeñas perturbaciones aleatorias debido al ruido.

```python
gaussian_signal= original_signal + gaussian_noise
```

*Visualización de la señal ruidosa usando matplot*

```python
mp.figure(figsize=(12,4))
mp.plot(time_10s, gaussian_signal[:num_muestras_10s], label='señal ruido gaussiano')
mp.grid()
mp.title('señal ruido gaussiano (cu01)')
mp.xlabel('Tiempo[s]')
mp.ylabel('Amplitud[mV]')
mp.show()
```

![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/RUIDO%20GAUS%201.jpg)

## **Calculo del SNR**

**¿Que es el  SNR?**

El SNR (Signal-to-Noise Ratio) es una medida que compara la potencia de la señal con la potencia del ruido. Se expresa en decibeles (dB) y nos indica qué tan clara es la señal en presencia de ruido.

En python la ecuacion del SNR:

```python
cuadrado_osignal = np.mean(original_signal**2)  # Potencia de la señal
cuadrado_ruido_gausiano = np.mean(gaussian_noise**2)  # Potencia del ruido

snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_gausiano)
print(f"SNR Gauss: {snr} dB")

SNR Gauss 1: 13.885570548616592 dB
```
**El SNR nos dice cuántas veces la señal es más fuerte que el ruido. Un SNR alto indica que la señal es clara y el ruido es bajo. Un SNR bajo indica que el ruido está afectando significativamente la señal.**

## **Para el ruido gaussiano 2**
En este caso lo unico que va cambiar es el valor de la desviacion estandar manteniendo el mismo codigo y visualizacion 

```python
media = 0      # Media de la distribución (el centro de la campana)
desviacion_estandar = 0.2  # Desviación estándar (el ancho de la campana)
longitud = len(original_signal)  # Longitud del array de ruido
gaussian_noise = np.random.normal(media, desviacion_estandar, longitud)

SNR Gauss 2: 7.8596475845341915 dB
```

![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Ruido%20Gaus%202.jpg)

## **Analisis de los ruidos gaussianos**
* **A mayor SNR, mejor calidad de la señal:** Un SNR de 13.89 dB indica que la señal sigue siendo clara, mientras que 7.87 dB sugiere que el ruido es más fuerte y afecta más la señal.
  
* **El ruido influye directamente en el SNR:** Al aumentar la desviación estándar del ruido (de 0.1 a 0.2), la potencia del ruido crece y el SNR disminuye, lo que hace que la señal sea menos distinguible.

## **6.2 Ruidos de Impulso**
Se define un ruido impulso con:

Número de impulsos = 100 → El ruido número de impulsos en la señal.

Amplitud del impulso = 5 → La amplitud del ruido lo suficientemente grande para ser observada en la gráfica.

Longitud = len(original_signal) → Se genera un ruido de la misma longitud que la señal original.

## **Para el ruido impulso 1**

```python
num_impulses = 100  # Número de impulsos
impulse_amplitude = 5  # Amplitud de los impulsos
impulse_noise = np.zeros(len(original_signal))# se crea un arreglo de ceros del tamaño de la señal original
impulse_positions = np.random.choice(len(original_signal), num_impulses, replace=False) #crea impulsos aleatorios
impulse_noise[impulse_positions] = impulse_amplitude #asigna la amplitud a las posiciones aleatorias  dentro del arreglo impulse_noise

impulse_signal = original_signal + impulse_noise

SNR Impulso: 10.943267544898685 dB
```

**visualización de la señal con matplot**
![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Ruido%20impulso%201.jpg)

## **Para el ruido impulso 2**
En este caso lo unico que va cambiar es el valor de la amplitud del impulso
```python
num_impulses = 100  # Número de impulsos
impulse_amplitude = 10  # Amplitud de los impulsos
impulse_noise = np.zeros(len(original_signal))# se crea un arreglo de ceros del tamaño de la señal original

SNR Impulso 2: 4.922667631619061 dB
```
**visualización de la señal con matplot**
![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Ruido%20impulso%202.jpg)

## **Analisis de los ruidos impulsos**
El cambio en el SNR se debe a que la potencia del ruido es proporcional al cuadrado de la amplitud del impulso. Al aumentar la amplitud, la potencia del ruido aumenta más rápidamente, lo que disminuye el SNR (peor relación señal a ruido.).

## **6.3 Ruidos de Artefacto**

Este código simula el efecto de la interferencia de la red eléctrica en una señal fisiológica. En muchos dispositivos electrónicos y biomédicos, se observa un ruido de 60 Hz debido a la corriente alterna (CA).

Aquí se presentan dos casos, con diferentes niveles de interferencia, y se calcula el SNR (Signal-to-Noise Ratio) para evaluar el impacto del ruido en la señal.


 ## **Ruido Artefacto 1**

**Generación del ruido**

* Se define un ruido de 60 Hz, que representa la interferencia eléctrica.
  
* La amplitud del ruido es de 0.1V, lo que significa que la interferencia es pequeña.

```python
# Frecuencia de la interferencia eléctrica (60 Hz)
i_frequency = 60  

# Amplitud del ruido artefacto
i_amplitude = 0.1  

# Generamos el ruido artefacto (una señal senoidal de 60 Hz)
device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * np.arange(len(original_signal)) / fs)
```


  **Suma del Ruido a la señal original**
  
  * Se suma la interferencia a la señal original, simulando una señal real afectada por artefactos eléctricos.
    
  ```python
  device_signal = original_signal + device_noise
  ```
  
   **Visualización de la señal ruidosa con funciones de matplotlib**
   
  ```python
  
  mp.figure(figsize=(12,4))
  mp.plot(time_10s, device_signal[:num_muestras_10s], label='Señal con ruido artefacto')
  mp.grid()
  mp.title('Señal con ruido artefacto (60 Hz, Amplitud 0.1V)')
  mp.xlabel('Tiempo [s]')
  mp.ylabel('Amplitud [mV]')
  mp.show()
  
  ```
  ![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Ruido%20artefacto%201.jpg)

**Cálculo del SNR**

* Se calcula la potencia de la señal y la potencia del ruido.
* Como la amplitud del ruido es baja, el SNR debe ser alto, indicando que la señal es más fuerte que el ruido.

```python
cuadrado_osignal = np.mean(original_signal**2)  
cuadrado_ruido_artefacto = np.mean(device_noise**2)  
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_artefacto)
print(f"SNR Artefacto 1: {snr} dB")

SNR Artefacto 1: 16.88703282121869 dB
```
## **Ruido Artefacto 2**

**Generación del ruido con mayor interferencia**

* Ahora, la amplitud del ruido es 0.5V, 5 veces mayor que en el primer caso.
  
* La interferencia es mucho más fuerte y afectará significativamente la señal.

```python

# Aumentamos la amplitud de la interferencia a 0.5V
i_amplitude = 0.5  

# Generamos el nuevo ruido de 60 Hz con mayor amplitud
device_noise = i_amplitude * np.sin(2 * np.pi * i_frequency * np.arange(len(original_signal)) / fs)
```
![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/Ruido%20artefacto%202.jpg)

## **Cálculo del SNR con mayor interferencia**

* Como la amplitud del ruido es mayor, el SNR será menor.

* Esto significa que la señal está mucho más afectada y será difícil de analizar sin filtros adecuados.
  
```python
cuadrado_osignal = np.mean(original_signal**2)  
cuadrado_ruido_artefacto = np.mean(device_noise**2)  
snr = 10 * np.log10(cuadrado_osignal / cuadrado_ruido_artefacto)
print(f"SNR Artefacto 2: {snr} dB")

SNR Artefacto 2 : 2.9076327344983124 dB
```

## **Analisis de ruido artefacto**

 **A mayor interferencia de 60 Hz, menor SNR.**

   * Con 0.1V de interferencia, la señal sigue siendo clara.
   * Con 0.5V de interferencia, la señal se distorsiona fuertemente.

   

Análisis adicional: Puedes agregar código para calcular características de la señal como frecuencia cardíaca, variabilidad de la frecuencia cardíaca, etc.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

##Licencia
Universidad Militar Nueva Granada
https://physionet.org/content/cudb/1.0.0/

