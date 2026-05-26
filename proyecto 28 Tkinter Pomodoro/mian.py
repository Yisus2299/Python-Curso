from tkinter import *
from pathlib import Path
import math

#==================== CONSTANTES ==============================================================================================================================#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO = Path(__file__).resolve().parent

#==================== TIMES RESET ==============================================================================================================================#

timer_after_id = None
reps = 0

#==================== TIMER MECHANISM ==========================================================================================================================#


def start_timer():
    global timer_after_id, reps
    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        cuenta_atras(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        cuenta_atras(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        cuenta_atras(work_sec)
        title_label.config(text="Work", fg=GREEN)


def reset_timer():
    global timer_after_id, reps
    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer", fg=GREEN)


#==================== COUNTDOWN MECHANISM ======================================================================================================================#


def cuenta_atras(count):
    global timer_after_id
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer_after_id = window.after(1000, cuenta_atras, count - 1)
    else:
        timer_after_id = None
        # reps impar = acaba de terminar un bloque de trabajo
        if reps % 2 == 1:
            n = (reps + 1) // 2
            check_marks.config(text="✔" * n)
        start_timer()


#==================== UI SETUP =================================================================================================================================#

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(window, width=300, height=324, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file=str(TOMATO / "tomato.png"))
canvas.create_image(150, 162, image=tomato_img)
timer_text = canvas.create_text(150, 162, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(window, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(window, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()