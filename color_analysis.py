import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import pyperclip
import webbrowser
from customtkinter import filedialog, CTkLabel as Label, CTkImage
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Color Analyzer")
app.geometry("900x700")
app.minsize(700, 500)
app.resizable(True, True)

# Variables globales
current_image = None

# Funciones
def open_discord():
    webbrowser.open("https://discord.gg/Mqw6BUZB3w")

def abrir_github():
    webbrowser.open("https://github.com/KenadderBOSS")

def copy_color(color):
    pyperclip.copy(color)

# Declaramos una variable global para guardar el ID de la imagen en el canvas
canvas_image_id = None
def kmeans_simple(pixels, n_colors=5, max_iters=10):
    # Inicialización aleatoria de los centroides
    unique_pixels = np.unique(pixels, axis=0)
    if len(unique_pixels) < n_colors:
        n_colors = len(unique_pixels)

    centroids = unique_pixels[np.random.choice(len(unique_pixels), size=n_colors, replace=False)]
    prev_centroids = np.zeros_like(centroids)

    for _ in range(max_iters):
        distances = np.linalg.norm(pixels[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        new_centroids = []
        for i in range(n_colors):
            assigned_pixels = pixels[labels == i]
            if len(assigned_pixels) == 0:
                # Reasignar centroides vacíos aleatoriamente
                new_centroids.append(pixels[np.random.randint(0, len(pixels))])
            else:
                new_centroids.append(assigned_pixels.mean(axis=0))
        
        new_centroids = np.array(new_centroids)
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids

    return centroids.astype(int), labels

def cargar_imagen():
    global current_image, canvas_image_id

    file_path = filedialog.askopenfilename(
        title="Color Analysis",
        filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp")]
    )
    
    if file_path:
        img = Image.open(file_path)

        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        max_size = min(canvas_width, canvas_height)
        img.thumbnail((max_size, max_size))

        img_tk = ImageTk.PhotoImage(img)

        # Eliminar imagen anterior si existe
        if canvas_image_id is not None:
            canvas.delete(canvas_image_id)

        # Mostrar la nueva imagen y guardar su ID
        canvas_image_id = canvas.create_image(0, 0, image=img_tk, anchor="nw")
        canvas.image = img_tk  # mantener referencia para evitar que se borre

        current_image = img
        extract_main_colors(file_path)

def extract_main_colors(image_path, n_colors=5):
    img = Image.open(image_path)
    img_data = np.array(img)
    pixels = img_data.reshape(-1, 3)
    pixels = pixels[np.all(pixels != [255, 255, 255], axis=1)]  # Excluir blancos

    if len(pixels) == 0:
        return

    
    main_colors, labels = kmeans_simple(pixels, n_colors)


    for widget in color_frame.winfo_children():
        widget.destroy()

    for color in main_colors:
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        btn = ctk.CTkButton(color_frame, text="", width=30, height=25, fg_color=hex_color,
                            command=lambda c=hex_color: copy_color(c))
        btn.pack(pady=5)

def tomar_color(event):
    if current_image:
        x, y = event.x, event.y
        color = current_image.getpixel((x, y))
        hex_color = "#{:02x}{:02x}{:02x}".format(*color)
        color_label.configure(fg_color=hex_color, text=f"RGB: {color}\nHex: {hex_color}")
        pyperclip.copy(hex_color)
zoom_canvas_image = None  # Referencia al objeto de imagen en el canvas

zoom_canvas_image = None  # Global para la imagen de zoom

def show_zoom(event):
    global zoom_canvas_image

    if current_image:
        crop_size = 50
        zoom_display_size = 100

        x, y = event.x, event.y
        left = max(x - crop_size // 2, 0)
        upper = max(y - crop_size // 2, 0)
        right = min(x + crop_size // 2, current_image.width)
        lower = min(y + crop_size // 2, current_image.height)

        if lower > upper and right > left:
            # Recorte y resize
            zoom_region = current_image.crop((left, upper, right, lower))
            zoom_region = zoom_region.resize((zoom_display_size, zoom_display_size), Image.LANCZOS)

            # Máscara circular
            zoom_region = zoom_region.convert("RGBA")
            mask = Image.new("L", (zoom_display_size, zoom_display_size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, zoom_display_size, zoom_display_size), fill=255)
            zoom_region.putalpha(mask)

            # Convertir a PhotoImage
            zoom_tk = ImageTk.PhotoImage(zoom_region)

            # Eliminar zoom anterior si existe
            if zoom_canvas_image:
                canvas.delete(zoom_canvas_image)

            # Crear nueva imagen sobre el canvas
            zoom_canvas_image = canvas.create_image(
                event.x, event.y, image=zoom_tk
            )
            canvas.zoom_tk = zoom_tk  # Guardar referencia para evitar GC

def hide_zoom(event):
    global zoom_canvas_image
    if zoom_canvas_image:
        canvas.delete(zoom_canvas_image)
        zoom_canvas_image = None

# Estructura visual
main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

left_frame = ctk.CTkFrame(main_frame, width=200)
left_frame.pack(side="left", fill="y", padx=10)

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", expand=True, fill="both")

# Botón Cargar Imagen
btn_cargar = ctk.CTkButton(left_frame, text="Cargar Imagen", command=cargar_imagen)
btn_cargar.pack(pady=10)

# Área para colores extraídos
color_frame = ctk.CTkFrame(left_frame)
color_frame.pack(pady=10, fill="x", expand=True)

# Canvas
canvas = ctk.CTkCanvas(right_frame, bd=0, highlightthickness=0)
canvas.pack(expand=True, fill="both", padx=10, pady=10)
canvas.bind("<Button-1>", tomar_color)
canvas.bind("<Motion>", show_zoom)
canvas.bind("<Leave>", hide_zoom)

# Zoom label
zoom_label = Label(master=canvas)
zoom_label.place_forget()

# Color label
color_label = Label(master=app, text="Haz clic en un píxel para ver el color", height=40)
color_label.pack(pady=5)

# Botones abajo
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(pady=10)

botondiscord = ctk.CTkButton(bottom_frame, text="Discord", command=open_discord)
botondiscord.pack(side="left", padx=10)

boton_github = ctk.CTkButton(bottom_frame, text="GitHub", command=abrir_github)
boton_github.pack(side="left", padx=10)

# Iniciar app
app.mainloop()
