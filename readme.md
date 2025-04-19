# Análisis de Colores en Imágenes

## **Descripción**

Este programa ha sido desarrollado por mí, un estudiante de seguridad informática. A medida que lo uses, puedes encontrar errores o áreas de mejora. El código está disponible públicamente, y agradezco cualquier consejo, optimización o reutilización de este proyecto en otros repositorios.

![coloranalyzergif](https://github.com/user-attachments/assets/94caccf8-8735-4175-be9a-96a32413c64b)

![coloranalyzergif2](https://github.com/user-attachments/assets/73216c5a-fb14-44dc-a169-29f07b9bf200)


## **¿Por qué usar esta aplicación?**

Hoy en día, existen muchas páginas web que ofrecen herramientas de análisis de colores o "color pickers", pero a menudo requieren que subas imágenes a servidores externos. Esto puede comprometer tu privacidad, especialmente si las imágenes son confidenciales o personales. 

Además, algunas de estas plataformas requieren registros o suscripciones, lo que puede resultar innecesario si solo planeas usar la herramienta una o dos veces. Estas plataformas también pueden solicitar datos personales, lo cual puede ser un inconveniente.

Este programa te permite realizar el análisis de colores **localmente**, sin necesidad de subir imágenes a servidores externos, lo que garantiza tu privacidad y evita el intercambio de datos personales. Está hecho 100% en Python por una sola persona y es compatible con Windows y Linux.

### **Funciona sin conexión a Internet**

## **Características**

- Carga imágenes en los formatos PNG, JPG, JPEG y BMP.
- Obtiene el color de cualquier píxel de la imagen.
- Convierte el color a formato hexadecimal.
- Copia automáticamente el código hexadecimal al portapapeles.

## **Instalación y Uso**

### **Usando la última Release (sin necesidad de instalación)**

Si solo deseas usar el programa sin modificar el código o clonar el repositorio, puedes descargar la última versión en formato `.exe` desde la página de releases.

1. Descarga la última release [aquí](https://github.com/KenadderBOSS/Color-Analyzer/releases).
2. Ejecuta el archivo `.exe` y comienza a analizar colores de imágenes.

### **Clonando el Repositorio (si deseas personalizar el programa)**

Si deseas clonar el repositorio y personalizar el programa, necesitarás instalar algunas dependencias.

1. Clona el repositorio:
    ```bash
    git clone https://github.com/KenadderBOSS/Color-Analyzer
    cd Color-Analyzer
    ```

2. Instala las dependencias utilizando el archivo `setup.py`:
    ```bash
    python3 setup.py install
    ```

3. Ejecuta el programa:
    ```bash
    python3 color_analyzer.py
    ```

### **Requisitos del Sistema**

Si decides clonar el repositorio y ejecutar el programa localmente, necesitarás tener las siguientes dependencias instaladas:

- Python 3.0 o superior
- `customtkinter`
- `Pillow`
- `pyperclip`
- `numpy`
- `scikit-learn`

Para instalar las dependencias, puedes usar el siguiente comando:
```bash
python3 setup.py install
```

### **Ejecución del Programa**

Una vez instalado, puedes ejecutar el programa con el siguiente comando:

```bash
python3 color_analyzer.py
```

Carga una imagen y haz clic sobre un píxel para obtener su color en formato hexadecimal, que se copiará automáticamente al portapapeles.

---

Si encuentras algún error o tienes preguntas sobre la instalación o el uso en otros sistemas operativos, no dudes en contactarme. ¡Estoy abierto a sugerencias y mejoras!

---

Ahora la instalación es más sencilla y compatible con ambos sistemas operativos. ¡Espero que te sea útil!
