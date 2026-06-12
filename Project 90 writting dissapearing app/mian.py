import tkinter as tk
import time

timeout = 5.0
last_activity = time.time()

root = tk.Tk()
root.title("Dangerous Writer")
root.geometry("800x500")

top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=6)

tk.Label(top_frame, text="Inactivity Timeout:").pack(side="left")
var = tk.StringVar(value="5")
def set_timeout(_=None):
    global timeout
    timeout = float(var.get())
tk.OptionMenu(top_frame, var, "5", "10", command=set_timeout).pack(side="left")

status = tk.Label(top_frame, text="Start typing...", fg="red")
status.pack(side="right")

text = tk.Text(root, wrap="word", font=("Segoe UI", 12))
text.pack(expand=True, fill="both", padx=8, pady=(0,8))

def on_key(event=None):
    global last_activity
    last_activity = time.time()
    status.config(text=f"Will delete after {timeout:.1f}s of inactivity")

text.bind("<Key>", on_key)

def tick():
    global last_activity
    remaining = timeout - (time.time() - last_activity)
    if remaining <= 0:
        content = text.get("1.0", "end-1c")
        if content:
            text.delete("1.0", "end")
            status.config(text="Deleted due to inactivity")
        last_activity = time.time()
    else:
        status.config(text=f"Delete in {remaining:.1f}s")
    root.after(100, tick)

tick()
root.mainloop()