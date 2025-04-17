import os
import platform
import subprocess

def install_requirements():
    # Detectar el sistema operativo
    current_os = platform.system()

    if current_os == "Windows":
        print("Sistema operativo: Windows")
        # Comando para Windows
        try:
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
            print("Dependencias instaladas con éxito en Windows.")
        except subprocess.CalledProcessError:
            print("Hubo un error al instalar las dependencias en Windows.")
    elif current_os == "Linux":
        print("Sistema operativo: Linux")
        # Comando para Linux
        try:
            # Instalar xclip y tkinter
            subprocess.run(["sudo", "apt-get", "install", "-y", "xclip", "python3-tk"], check=True)
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
            print("Dependencias instaladas con éxito en Linux.")
        except subprocess.CalledProcessError:
            print("Hubo un error al instalar las dependencias en Linux.")
    else:
        print(f"Sistema operativo no soportado: {current_os}")

if __name__ == "__main__":
    install_requirements()
