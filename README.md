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
1. **Instalacion librerias**
    
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

2. **Usando la web physionet descarga un archivo de ECG:**

Coloca el archivo .hea y .dat (por ejemplo, cu01.hea, cu01.dat) en la misma carpeta que el script de Python.
esto para evitar 


3. **Selección del canal:** Modifica el índice dentro de signal = record.p_signal[:,0] para seleccionar un canal diferente si el registro tiene múltiples canales.
 
4. **Personalización del gráfico:** Utiliza las funciones de matplotlib para personalizar el aspecto del gráfico (colores, etiquetas, límites, etc.).
   ```python
   
   mp.figure(figsize=(12, 4))
   mp.plot(time, signal, label='Señal original')
   mp.title('Señal Fisiológica (cu01)')
   mp.xlabel('Tiempo (s)')
   mp.ylabel('Voltaje(mv)')
   mp.legend()
   mp.grid()
   ```
5. **

   

Análisis adicional: Puedes agregar código para calcular características de la señal como frecuencia cardíaca, variabilidad de la frecuencia cardíaca, etc.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

##Licencia
Universidad Militar Nueva Granada
https://physionet.org/content/cudb/1.0.0/

