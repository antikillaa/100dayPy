import datetime
import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text=get_time_from_seconds(0))
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(foreground=RED, text="Break")
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(foreground=PINK, text="Break")
    else:
        count_down(work_sec)
        timer_label.config(foreground=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(t):
    canvas.itemconfig(canvas_text, text=get_time_from_seconds(t))
    global timer
    if t > 0:
        timer = window.after(1000, count_down, t - 1)
    else:
        start_timer()
        check_marks.config(text="✓" * round(reps / 2))


def get_time_from_seconds(sec):
    return time.strftime("%M:%S", time.gmtime(sec))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40), background=YELLOW, foreground=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text=get_time_from_seconds(0), fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_button)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
