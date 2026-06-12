import tkinter as tk
from tkinter import Tk, Button, Entry, Label, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

def rgb_a_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

class AppWatermark:
    def __init__(self, root):
        self.root = root
        self.image = None
        self.photo = None

        bg_color = rgb_a_hex(30, 30, 40)

        root.configure(bg=bg_color)

        frame = tk.Frame(root, bg=bg_color)
        frame.pack(fill="both", expand=True)

        self.entry = Entry(frame, width=40, bg=bg_color, fg="white")
        self.entry.pack(pady=5)
        self.entry.insert(0, "© My Name")

        Button(frame, text="Open Image", command=self.open_image).pack(pady=5)
        Button(frame, text="Apply Watermark", command=self.apply_watermark).pack(pady=5)

        Button(frame, text="Save", command=self.save).pack(pady=5)
        self.preview = Label(frame, bg=bg_color)
        self.preview.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if not path:
            return
        self.image = Image.open(path).convert("RGBA")
        self.show_preview(self.image)

    def apply_watermark(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Open an image first")
            return
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Enter watermark text")
            return

        layer = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except OSError:
            font = ImageFont.load_default()
        draw.text((20, 20), text, fill=(255, 255, 255, 160), font=font)

        self.image = Image.alpha_composite(self.image, layer)
        self.show_preview(self.image)

    def show_preview(self, img):
        copy = img.copy()
        copy.thumbnail((500, 500))
        self.photo = ImageTk.PhotoImage(copy)
        self.preview.configure(image=self.photo)

    def save(self):
        if self.image is None:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if not path:
            return
        out = self.image
        if path.lower().endswith((".jpg", ".jpeg")):
            out = self.image.convert("RGB")
        out.save(path)
        messagebox.showinfo("Done", "Image saved")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Watermark")
    AppWatermark(root)
    root.mainloop()