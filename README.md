# Laboratorio1-Se-ales

# Visualizador de Señales Electrocardiográficas (ECG)

Este repositorio contiene un script de Python simple para cargar y visualizar señales electrocardiográficas (ECG) a partir de archivos .hea y .dat de PhysioNet.

## Requisitos
* **Python:** Se requiere una instalación de Python 3.x.
* **Bibliotecas:**
  * `wfdb`: Para leer archivos de PhysioNet.
  * `matplotlib`: Para crear gráficos.
  * `numpy`: Para realizar operaciones numéricas.

## Instalación
1. **Clonar el repositorio:**
   git clone [se quitó una URL no válida]

Asegúrate de crear un archivo requirements.txt con las siguientes líneas:
wfdb
matplotlib
numpy
Uso
Coloca el archivo .hea (por ejemplo, cu01.hea) en la misma carpeta que el script de Python.
Ejecuta el script:
Bash

python tu_script.py
Personalización
Selección del canal: Modifica el índice dentro de signal = record.p_signal[:,0] para seleccionar un canal diferente si el registro tiene múltiples canales.
Personalización del gráfico: Utiliza las funciones de matplotlib para personalizar el aspecto del gráfico (colores, etiquetas, límites, etc.).
Análisis adicional: Puedes agregar código para calcular características de la señal como frecuencia cardíaca, variabilidad de la frecuencia cardíaca, etc.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

Licencia
Universidad Militar Nueva Granada
