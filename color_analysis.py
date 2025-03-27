import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas, messagebox
from PIL import Image, ImageTk
import pyperclip
import webbrowser

def open_discord():
    discord_url = "https://discord.gg/Mqw6BUZB3w" # Mi grupo de discord
    webbrowser.open(discord_url)  # Abre la URL en el navegador

# Función para cargar la imagen
def load_image():
    """Abre un cuadro de diálogo para seleccionar una imagen y cargarla."""
    file_path = filedialog.askopenfilename(title="Color Analysis", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")])
    
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Redimensiona para ajustarse al tamaño de la ventana
        img_tk = ImageTk.PhotoImage(img)
        
        # Mostrar la imagen en la interfaz
        canvas.create_image(0, 0, image=img_tk, anchor="nw")
        canvas.image = img_tk  # Mantener la referencia de la imagen
        
        # Guardamos la imagen para poder acceder a ella cuando se haga clic
        global current_image
        current_image = img

# Función para obtener el color del píxel al hacer clic
def get_color(event):
    """Obtiene el color del píxel en la posición donde se hace clic."""
    if current_image:
        # Obtener las coordenadas donde se hizo clic
        x, y = event.x, event.y
        
        # Obtener el color del píxel en esas coordenadas
        color = current_image.getpixel((x, y))
        
        # Convertir el color a formato hexadecimal
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        
        # Mostrar el color y su valor hexadecimal
        color_label.config(bg=hex_color, text=f"Color RGB: {color}\nColor Hex: {hex_color}")
        
        # Copiar al portapapeles
        pyperclip.copy(hex_color)

# Función para abrir el perfil de GitHub
def open_github():
    """Abre el perfil de GitHub en el navegador."""
    webbrowser.open("https://github.com/KenadderBOSS")  # Cambia por tu URL de GitHub

# Función para abrir la sección de soporte de GitHub
def open_support():
    """Abre la sección de soporte de GitHub en el navegador."""
    webbrowser.open("https://github.com/KenadderBOSS/Color-Analyzer/issues")  # Cambia por la URL de soporte

# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Color Analysis")
root.iconbitmap("icono.ico")

# Estilo de la ventana
root.configure(bg="#f0f0f0")  # Fondo claro
root.geometry("500x600")  # Tamaño de la ventana

# Header con tu foto y nombre
header_frame = tk.Frame(root, bg="#f0f0f0")
header_frame.pack(fill="x", pady=10)
header = tk.Label(root, font=("Arial", 24))
header.pack(pady=20)
header_frame.configure(bg="black")
discord_button = tk.Button(header_frame, text="Discord", command=open_discord, font=("Helvetica Neue", 12), fg="white", bg="#5865F2", relief="flat", activebackground="#4752C4", cursor="hand2")
discord_button.pack(side="right", padx=10)








# Imagen de tu GitHub
github_image = Image.open("126710096.png")  # Asegúrate de colocar tu foto en el directorio correcto
github_image = github_image.resize((40, 40))  # Tamaño de la foto
github_image_tk = ImageTk.PhotoImage(github_image)

github_label = tk.Label(header_frame, image=github_image_tk, bg="#f0f0f0")
github_label.pack(side="left", padx=10)

# Nombre de usuario y enlace a GitHub
github_name = "@KenadderBOSS"  # Cambia con tu nombre de usuario en GitHub
github_name_label = tk.Label(header_frame, text=github_name, font=("Helvetica Neue", 14, "bold"), fg="#FFFFFF", bg="#000000", cursor="hand2")
github_name_label.pack(side="left")
github_name_label.bind("<Button-1>", lambda e: open_github())  # Redirige al perfil de GitHub

# Crear un canvas para mostrar la imagen
canvas = tk.Canvas(root, width=400, height=400, bg="#ffffff", bd=0, highlightthickness=0)
canvas.pack(padx=10, pady=10)

# Crear un botón para cargar la imagen
load_button = tk.Button(root, text="Cargar Imagen", command=load_image, font=("Helvetica Neue", 14), fg="white", bg="#007BFF", relief="flat", activebackground="#0056b3")
load_button.pack(pady=10)

# Crear un label para mostrar el color
color_label = Label(root, text="Haz clic en un píxel de la imagen", width=30, height=5, bg="#f0f0f0", fg="#333333", font=("Helvetica Neue", 12))
color_label.pack(padx=10, pady=20)

# Crear un botón de ayuda
help_button = tk.Button(root, text="Ayuda", command=open_support, font=("Helvetica Neue", 12), fg="white", bg="#007BFF", relief="flat", activebackground="#0056b3")
help_button.pack(pady=10)

# Asociar el evento de clic con la función de obtener el color
canvas.bind("<Button-1>", get_color)

# Variable para almacenar la imagen cargada
current_image = None

def on_enter(e):
    load_button.config(bg="#0056b3")  # Azul más oscuro al pasar el mouse

def on_leave(e):
    load_button.config(bg="#007BFF")  # Azul original al salir el mouse

def on_click(e):
    load_button.config(bg="#003d80")  # Azul más oscuro al hacer clic
    root.after(150, lambda: load_button.config(bg="#0056b3"))  # Vuelve al hover después de 150ms

# Asociar eventos al botón
load_button.bind("<Enter>", on_enter)
load_button.bind("<Leave>", on_leave)
load_button.bind("<Button-1>", on_click)


icono = Image.open("icono.png")  # Usa un PNG de 32x32 o 64x64
icono = ImageTk.PhotoImage(icono)

# Aplicar el icono correctamente
root.wm_iconphoto(True, icono)

# Ejecutar la aplicación
root.mainloop()
