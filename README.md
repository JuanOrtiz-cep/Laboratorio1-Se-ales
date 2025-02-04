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

 
# *3. Personalización del gráfico: Utiliza las funciones de matplotlib para personalizar el aspecto del gráfico (colores, etiquetas, límites, etc.).*
   
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

# *4. Datos estadisticos y Historigrama*
   
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

## **Ya con todo esto , se crea una interfaz para el historigrama con las funciones de matplotlib similares al punto 3**

![](https://github.com/JuanOrtiz-cep/Laboratorio1-Se-ales/blob/main/155112a9-58bf-45c5-82b3-6cde9e2dfb59.jpg)
   

Análisis adicional: Puedes agregar código para calcular características de la señal como frecuencia cardíaca, variabilidad de la frecuencia cardíaca, etc.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

##Licencia
Universidad Militar Nueva Granada
https://physionet.org/content/cudb/1.0.0/

