import tkinter as tk
from tkinter import Tk, Button, Entry, Label, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

def rgb_a_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

class AppMarcaAgua:
    def __init__(self, root):
        self.root = root
        self.imagen = None
        self.photo = None

        color_fondo = rgb_a_hex(30, 30, 40)

        root.configure(bg=color_fondo)

        frame = tk.Frame(root, bg=color_fondo)
        frame.pack(fill="both", expand=True)

        self.entry = Entry(frame, width=40, bg=color_fondo, fg="white")
        self.entry.pack(pady=5)
        self.entry.insert(0, "© Mi nombre")

        Button(frame, text="Abrir imagen", command=self.abrir).pack(pady=5)
        Button(frame, text="Aplicar marca", command=self.aplicar).pack(pady=5)

        Button(frame, text="Guardar", command=self.guardar).pack(pady=5)
        self.preview = Label(frame, bg=color_fondo)
        self.preview.pack()

    def abrir(self):
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg")])
        if not ruta:
            return
        self.imagen = Image.open(ruta).convert("RGBA")
        self.mostrar_preview(self.imagen)

    def aplicar(self):
        if self.imagen is None:
            messagebox.showwarning("Aviso", "Primero abre una imagen")
            return
        texto = self.entry.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Escribe un texto")
            return

        capa = Image.new("RGBA", self.imagen.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(capa)
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except OSError:
            font = ImageFont.load_default()
        draw.text((20, 20), texto, fill=(255, 255, 255, 160), font=font)

        self.imagen = Image.alpha_composite(self.imagen, capa)
        self.mostrar_preview(self.imagen)

    def mostrar_preview(self, img):
        copia = img.copy()
        copia.thumbnail((500, 500))
        self.photo = ImageTk.PhotoImage(copia)
        self.preview.configure(image=self.photo)

    def guardar(self):
        if self.imagen is None:
            return
        ruta = filedialog.asksaveasfilename(defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if not ruta:
            return
        salida = self.imagen
        if ruta.lower().endswith((".jpg", ".jpeg")):
            salida = self.imagen.convert("RGB")
        salida.save(ruta)
        messagebox.showinfo("Listo", "Imagen guardada")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Marca de agua")
    AppMarcaAgua(root)
    root.mainloop()