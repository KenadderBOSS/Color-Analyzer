# EN CONSTRUCCIÓN

Este programa esta hecho solo por mi, un estudiante de seguridad informática, es posible que encuentres errores, puedes ver el código del programa en todo momento y aceptaré consejos, optimizaciones o reutilización de este código en otro repositorio. 

# ¿Para qué?
Hoy en día, muchas páginas web ofrecen herramientas de análisis de colores o "color pickers", pero suelen requerir que subas imágenes a bases de datos externas. Esto puede no ser ideal por varias razones, especialmente cuando se trata de imágenes confidenciales o muy personales. Al utilizar estas plataformas, puedes estar comprometiendo tu privacidad al compartir imágenes sensibles sin una protección adecuada.

Algunas de estas plataformas también requieren registros o suscripciones para acceder a funciones adicionales. Esto puede ser innecesario si solo planeas utilizar la herramienta una o dos veces, además de que pueden pedirte datos personales como parte del proceso.

Esta aplicación está diseñada con fines de seguridad personal y práctica. Con ella, puedes realizar el análisis de colores sin necesidad de subir tus imágenes a servidores de terceros, lo que te permite mantener tu privacidad y evitar el intercambio de datos personales. Además, está hecha 100% en Python por una sola persona y es exclusiva para Windows por ahora. No se ha probado su funcionamiento en Linux.

Al utilizar esta aplicación, tienes el control total sobre tus imágenes y tus datos. No hay registros, suscripciones ni necesidad de compartir nada con plataformas externas.

### FUNCIONA SIN INTERNET

# Aplicación de Análisis de Colores en Imágenes

Este programa analiza una imagen y extrae los colores predominantes. Utiliza la librería `Pillow` para manejar imágenes y `matplotlib` para visualizar los resultados.

# Características

+ Carga de imágenes en formatos PNG, JPG, JPEG y BMP.

+ Obtención del color de cualquier píxel de la imagen.

+ Conversión del color a formato hexadecimal.

+ Copia automática del código hexadecimal al portapapeles.

## 1 Instalación y Uso | Windows y Linux
Descarga la ultima release y ejecuta el archivo .exe .

## 1.1 Clonando el repositorio el repositorio | Instalación y Uso | Windows 

Opción 1. Descarga la ultima [🔗 release](https://github.com/KenadderBOSS/Color-Analyzer/releases)

Opción 2. Clona este repositorio:
```bash
git clone https://github.com/KenadderBOSS/Color-Analyzer
cd Color-Analyzer
```
## 1.2 Clonando el repositorio Instalación y Uso | Ubuntu/Linux
Probado en Ubuntu 24.02 y funciona correctamente siguiendo los pasos a continuación


Clonar repositorio
```
git clone https://github.com/KenadderBOSS/Color-Analyzer
cd Color_Analyzer
```

Crear un entorno virtual para Python

```
python3 -m venv color_analyzer

source color_analyzer/bin/activate
```

Ejecutar setup.py para instalar dependencias

``` 
python3 setup.py
``` 
Lanzar Programa
```
python3 color_analysis.py
``` 

#### 2 Ejecuta el script en Python:
```bash

python color_analyzer.py
```
 
Carga una imagen y haz clic sobre un píxel para obtener su color.

# Requisitos
+ python 3.0 o +
+ customtkinter
+ pillow
+ pyperclip
+ numpy
+ scikit-learn

Si estas en otro sistema operativo y tienes algún error, hazmelo saber.