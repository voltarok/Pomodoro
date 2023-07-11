from tkinter import *
import math
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
timer = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_Label.config(text="Timer",fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_Label.config(text="long Break", fg=RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        title_Label.config(text="Short Break", fg=PINK)
    else :
        count_down(work_sec)
        title_Label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else :
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)
        # if reps % 2 == 0:
        #     marks += "✔"
        # checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_Label = Label(text="Timer", fg=GREEN, bg = YELLOW, font=(FONT_NAME, 40, "bold"))
title_Label.grid(column=1, row=0)

canvas = Canvas(width=200, height=275, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 152, image=tomato_image)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 175, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))


start_button = Button(text="start",width=5,command=start_timer)
start_button.grid(column=0, row=6)

reset_button = Button(text="reset",width=5,command=reset_timer)
reset_button.grid(column=6, row=6)

checkmarks = Label(fg=GREEN,highlightthickness=0,bg=YELLOW,font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=6)

window.mainloop()