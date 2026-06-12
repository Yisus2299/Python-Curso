import tkinter as tk
from tkinter import messagebox
import time

SAMPLE_TEXT = (
    "Sometimes you need to go backwards and then forward to keep it up "
)

def rgb_a_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

class AppSpeedTest:
    def __init__(self, root):
        self.root = root
        root.title("Typing Speed Test")
        root.geometry("700x400")

        bg_color = rgb_a_hex(30, 30, 40)

        root.configure(bg=bg_color)

        frame = tk.Frame(root, bg=bg_color)
        frame.pack(fill="both", expand=True)

        self.target_text = SAMPLE_TEXT.strip()
        self.active = False
        self.start_time = None
        self.duration = 60  # seconds
        self.time_left = self.duration

        tk.Label(root, text="Type the text below as quickly and accurately as you can:",
                 font=("Arial", 11)).pack(pady=8)

        self.lbl_sample = tk.Label(
            root, text=self.target_text, wraplength=650,
            justify="left", bg="#2a2a35", fg="white", padx=10, pady=10
        )
        self.lbl_sample.pack(fill="x", padx=15)

        self.textbox = tk.Text(root, height=6, font=("Consolas", 12))
        self.textbox.pack(fill="both", expand=True, padx=15, pady=8)
        self.textbox.bind("<KeyRelease>", self.on_type)
        self.textbox.config(state="disabled")

        frame_info = tk.Frame(root)
        frame_info.pack(pady=5)
        self.lbl_timer = tk.Label(frame_info, text="Time: 60 s", font=("Arial", 12, "bold"))
        self.lbl_timer.pack(side="left", padx=15)
        self.lbl_wpm = tk.Label(frame_info, text="WPM: 0", font=("Arial", 12, "bold"))
        self.lbl_wpm.pack(side="left", padx=15)
        self.lbl_accuracy = tk.Label(frame_info, text="Accuracy: 0%", font=("Arial", 12))
        self.lbl_accuracy.pack(side="left", padx=15)

        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)
        tk.Button(frame_btn, text="Start", width=12, command=self.start).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Reset", width=12, command=self.reset).pack(side="left", padx=5)

    def correct_chars(self, target, typed):
        """Count correct characters in order (like 'corrected CPM')."""
        return sum(1 for a, b in zip(typed, target) if a == b)

    def calculate_wpm(self, typed, seconds):
        if seconds <= 0:
            return 0
        correct = self.correct_chars(self.target_text, typed)
        minutes = seconds / 60
        return int((correct / 5) / minutes)

    def calculate_accuracy(self, typed):
        if not typed:
            return 0
        correct = self.correct_chars(self.target_text, typed)
        return int((correct / len(typed)) * 100)

    def start(self):
        self.reset(no_message=True)
        self.active = True
        self.start_time = time.time()
        self.textbox.config(state="normal")
        self.textbox.focus()
        self.tick()

    def reset(self, no_message=False):
        self.active = False
        self.start_time = None
        self.time_left = self.duration
        self.textbox.config(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.config(state="disabled")
        self.lbl_timer.config(text=f"Time: {self.duration} s")
        self.lbl_wpm.config(text="WPM: 0")
        self.lbl_accuracy.config(text="Accuracy: 0%")

    def tick(self):
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        self.time_left = max(0, self.duration - int(elapsed))
        self.lbl_timer.config(text=f"Time: {self.time_left} s")

        typed = self.textbox.get("1.0", "end-1c")
        self.lbl_wpm.config(text=f"WPM: {self.calculate_wpm(typed, elapsed)}")
        self.lbl_accuracy.config(text=f"Accuracy: {self.calculate_accuracy(typed)}%")

        if self.time_left <= 0:
            self.finish()
        else:
            self.root.after(200, self.tick)

    def on_type(self, event=None):
        if not self.active:
            return
        typed = self.textbox.get("1.0", "end-1c")
        if len(typed) >= len(self.target_text):
            self.finish()

    def finish(self):
        if not self.active:
            return
        self.active = False
        self.textbox.config(state="disabled")

        typed = self.textbox.get("1.0", "end-1c")
        seconds = min(self.duration, time.time() - self.start_time)
        wpm = self.calculate_wpm(typed, seconds)
        accuracy = self.calculate_accuracy(typed)

        if wpm < 40:
            level = "Below average (~40 WPM). Keep practicing!"
        elif wpm < 60:
            level = "Average speed. You're doing fine."
        elif wpm < 80:
            level = "Above average. Very good."
        elif wpm < 100:
            level = "Advanced level. Excellent."
        else:
            level = "Amazing! Expert level (100+ WPM)."

        messagebox.showinfo(
            "Result",
            f"WPM: {wpm}\nAccuracy: {accuracy}%\n\n{level}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    AppSpeedTest(root)
    root.mainloop()