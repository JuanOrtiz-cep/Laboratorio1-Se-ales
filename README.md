# Laboratorio 1 Señales

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

**toma los valores de la señal y los organiza en 100 grupos para calcular la probabilidad de ocurrencia de cada valor. A continuación, explicamos cada línea del código.**

```python
min_val = min(original_signal)  # Valor mínimo de la señal
```

**Se obtiene el valor mínimo de la señal, que será el límite inferior del rango en el que se agruparán los valores.**

```python
max_val = max(original_signal)  # Encuentra el valor más grande en la señal
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
 

Análisis adicional: Puedes agregar código para calcular características de la señal como frecuencia cardíaca, variabilidad de la frecuencia cardíaca, etc.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

##Licencia
Universidad Militar Nueva Granada
https://physionet.org/content/cudb/1.0.0/

