import tkinter as tk
from tkinter import messagebox
import time

TEXTO_MUESTRA = (
    "Sometimes you need to go backwards and then fordward to keep it up "
)

def rgb_a_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

class AppSpeedTest:
    def __init__(self, root):
        self.root = root
        root.title("Test de velocidad de escritura")
        root.geometry("700x400")

        color_fondo = rgb_a_hex(30, 30, 40)

        root.configure(bg=color_fondo)

        frame = tk.Frame(root, bg=color_fondo)
        frame.pack(fill="both", expand=True)

        self.texto_objetivo = TEXTO_MUESTRA.strip()
        self.activo = False
        self.inicio = None
        self.duracion = 60  # segundos
        self.tiempo_restante = self.duracion

        tk.Label(root, text="Escribe el texto de abajo lo más rápido y preciso que puedas:",
                 font=("Arial", 11)).pack(pady=8)

        self.lbl_muestra = tk.Label(
            root, text=self.texto_objetivo, wraplength=650,
            justify="left", bg="#2a2a35", fg="white", padx=10, pady=10
        )
        self.lbl_muestra.pack(fill="x", padx=15)

        self.caja = tk.Text(root, height=6, font=("Consolas", 12))
        self.caja.pack(fill="both", expand=True, padx=15, pady=8)
        self.caja.bind("<KeyRelease>", self.al_escribir)
        self.caja.config(state="disabled")

        frame_info = tk.Frame(root)
        frame_info.pack(pady=5)
        self.lbl_timer = tk.Label(frame_info, text="Tiempo: 60 s", font=("Arial", 12, "bold"))
        self.lbl_timer.pack(side="left", padx=15)
        self.lbl_wpm = tk.Label(frame_info, text="WPM: 0", font=("Arial", 12, "bold"))
        self.lbl_wpm.pack(side="left", padx=15)
        self.lbl_precision = tk.Label(frame_info, text="Precisión: 0%", font=("Arial", 12))
        self.lbl_precision.pack(side="left", padx=15)

        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)
        tk.Button(frame_btn, text="Iniciar", width=12, command=self.iniciar).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Reiniciar", width=12, command=self.reiniciar).pack(side="left", padx=5)

    def caracteres_correctos(self, objetivo, escrito):
        """Cuenta caracteres correctos en orden (como 'corrected CPM')."""
        return sum(1 for a, b in zip(escrito, objetivo) if a == b)

    def calcular_wpm(self, escrito, segundos):
        if segundos <= 0:
            return 0
        correctos = self.caracteres_correctos(self.texto_objetivo, escrito)
        minutos = segundos / 60
        return int((correctos / 5) / minutos)

    def calcular_precision(self, escrito):
        if not escrito:
            return 0
        correctos = self.caracteres_correctos(self.texto_objetivo, escrito)
        return int((correctos / len(escrito)) * 100)

    def iniciar(self):
        self.reiniciar(sin_mensaje=True)
        self.activo = True
        self.inicio = time.time()
        self.caja.config(state="normal")
        self.caja.focus()
        self.tick()

    def reiniciar(self, sin_mensaje=False):
        self.activo = False
        self.inicio = None
        self.tiempo_restante = self.duracion
        self.caja.config(state="normal")
        self.caja.delete("1.0", "end")
        self.caja.config(state="disabled")
        self.lbl_timer.config(text=f"Tiempo: {self.duracion} s")
        self.lbl_wpm.config(text="WPM: 0")
        self.lbl_precision.config(text="Precisión: 0%")

    def tick(self):
        if not self.activo:
            return
        transcurrido = time.time() - self.inicio
        self.tiempo_restante = max(0, self.duracion - int(transcurrido))
        self.lbl_timer.config(text=f"Tiempo: {self.tiempo_restante} s")

        escrito = self.caja.get("1.0", "end-1c")
        self.lbl_wpm.config(text=f"WPM: {self.calcular_wpm(escrito, transcurrido)}")
        self.lbl_precision.config(text=f"Precisión: {self.calcular_precision(escrito)}%")

        if self.tiempo_restante <= 0:
            self.finalizar()
        else:
            self.root.after(200, self.tick)

    def al_escribir(self, event=None):
        if not self.activo:
            return
        escrito = self.caja.get("1.0", "end-1c")
        if len(escrito) >= len(self.texto_objetivo):
            self.finalizar()

    def finalizar(self):
        if not self.activo:
            return
        self.activo = False
        self.caja.config(state="disabled")

        escrito = self.caja.get("1.0", "end-1c")
        segundos = min(self.duracion, time.time() - self.inicio)
        wpm = self.calcular_wpm(escrito, segundos)
        precision = self.calcular_precision(escrito)

        if wpm < 40:
            nivel = "Por debajo del promedio (~40 WPM). ¡Sigue practicando!"
        elif wpm < 60:
            nivel = "Velocidad promedio. Vas bien."
        elif wpm < 80:
            nivel = "Por encima del promedio. Muy bien."
        elif wpm < 100:
            nivel = "Nivel avanzado. Excelente."
        else:
            nivel = "¡Increíble! Nivel experto (100+ WPM)."

        messagebox.showinfo(
            "Resultado",
            f"WPM: {wpm}\nPrecisión: {precision}%\n\n{nivel}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    AppSpeedTest(root)
    root.mainloop()