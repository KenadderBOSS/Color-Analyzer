import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import pyperclip
import webbrowser
from customtkinter import filedialog, CTkLabel as Label, CTkImage
import numpy as np
from sklearn.cluster import KMeans

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")
app.resizable(False, False)

#####
def open_discord():
    discord_url = "https://discord.gg/Mqw6BUZB3w"
    webbrowser.open(discord_url)

def abrir_github():
    github_url = "https://github.com/KenadderBOSS"
    webbrowser.open(github_url)

def cargar_imagen():
    file_path = filedialog.askopenfilename(title="Color Analysis", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")])
    
    if file_path:
        
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)

        canvas.create_image(0, 0, image=img_tk, anchor="nw")
        canvas.image = img_tk
        
        global current_image
        current_image = img
        
        # Extraer los colores principales
        extract_main_colors(file_path)
        


def extract_main_colors(image_path, n_colors=5):
    img = Image.open(image_path)
    img_data = np.array(img)
    pixels = img_data.reshape(-1, 3)
    pixels = pixels[np.all(pixels != [255, 255, 255], axis=1)]  # Remover blanco

    if len(pixels) == 0:
        return  # No hay suficientes datos para analizar colores

    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    main_colors = kmeans.cluster_centers_.astype(int)

    # Eliminar cualquier colors_frame anterior
    global colors_frame
    if 'colors_frame' in globals():
        colors_frame.destroy()

    # Crear un nuevo colors_frame solo si hay colores que mostrar
    colors_frame = ctk.CTkFrame(master=app, width=200, height=300)
    colors_frame.place(relx=0.05, rely=0.15, anchor=ctk.NW)

    # Mostrar los colores principales en la lista
    for color in main_colors:
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

        color_button = ctk.CTkButton(colors_frame, 
                                     text=f"   ",  
                                     width=20, 
                                     height=2, 
                                     fg_color=hex_color, 
                                     command=lambda color=hex_color: copy_color(color))
        color_button.pack(pady=2)




def copy_color(color):
    pyperclip.copy(color)

def tomar_color(event):
    if current_image:
        x, y = event.x, event.y
        color = current_image.getpixel((x, y))
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        
        color_label.configure(fg_color=hex_color, text=f"Color RGB: {color}\nColor Hex: {hex_color}")
        pyperclip.copy(hex_color)

def show_zoom(event):
    if current_image:
        zoom_size = 50
        x, y = event.x, event.y
        left = max(x - zoom_size // 5, 0)
        upper = max(y - zoom_size // 5, 0)
        right = min(x + zoom_size // 5, current_image.width)
        lower = min(y + zoom_size // 5, current_image.height)
        
        if lower > upper and right > left:
            zoom_region = current_image.crop((left, upper, right, lower)).resize((100, 100))

            draw = ImageDraw.Draw(zoom_region)
            center_x, center_y = 50, 50

            # Dibujar la cruz (+) en el centro
            draw.line((center_x - 10, center_y, center_x + 10, center_y), fill="black", width=2)  # Línea horizontal
            draw.line((center_x, center_y - 10, center_x, center_y + 10), fill="black", width=2)  # Línea vertical

            zoom_ctk = CTkImage(zoom_region)
            zoom_label.configure(image=zoom_ctk)
            zoom_label.image = zoom_ctk
            zoom_label.place(x=event.x - zoom_size // 2, y=event.y - zoom_size // 2)
            zoom_label.configure(text="")


def hide_zoom(event):
    zoom_label.place_forget()

#####

canvas = ctk.CTkCanvas(master=app, width=400, height=400, bd=0, highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

color_label = Label(master=app, text="Haz clic en un píxel de la imagen", width=30, height=5, font=("Helvetica Neue", 12))
color_label.place(relx=0.5, rely=0.8, anchor=ctk.S)

zoom_label = Label(master=app, width=100, height=100)
zoom_label.place_forget()

canvas.bind("<Button-1>", tomar_color)
canvas.bind("<Motion>", show_zoom)
canvas.bind("<Leave>", hide_zoom)

current_image = None

# Contenedor para los botones de colores principales


botondiscord = ctk.CTkButton(master=app, text="Discord", command=open_discord)
botondiscord.place(relx=0.3, rely=0.9, anchor=ctk.S)

boton_github = ctk.CTkButton(master=app, text="Github", command=abrir_github)
boton_github.place(relx=0.7, rely=0.9, anchor=ctk.S)

button = ctk.CTkButton(master=app, text="Cargar Imagen", command=cargar_imagen)
button.place(relx=0.5, rely=0.15, anchor=ctk.N)

app.mainloop()