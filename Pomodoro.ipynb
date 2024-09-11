import customtkinter as ctk
import math
from PIL import Image, ImageTk

# -----------------------------CONSTANTS---------------------------- #
LIGHT_YELLOW = "#FCFCF7"
LIGHT_BEIGE = "#ECDCAB"
YELLOW_BEIGE = "#DFC57B"
GOLDEN_BROWN = "#BF932A"
DARK_BROWN = "#9E6200"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ---------------------------- #
# Resets the timer to default, cancels the ongoing countdown, and resets the session counter.
def reset_timer():
    window.after_cancel(timer)
    timer_label.configure(timer_label, text="00:00")
    title_label.configure(text="Timer", text_color=DARK_BROWN)
    check_marks.configure(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------- #
# Starts the timer and determines whether to initiate work or break sessions based on the rep count.
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.configure(text="Break", text_color=GOLDEN_BROWN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.configure(text="Break", text_color=YELLOW_BEIGE)
    else:
        count_down(work_sec)
        title_label.configure(text="Work", text_color=DARK_BROWN)

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
# Handles the countdown mechanism and updates the UI accordingly.
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.configure(timer_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.configure(text=marks)

# ---------------------------- UI SETUP -------------------------------- #
# Set up the appearance and layout of the window.
# ctk.set_appearance_mode("light")  # or "dark"
# ctk.set_default_color_theme("blue")  # You can choose other themes as well

window = ctk.CTk()
window.title("Pomodoro")
window.geometry("500x400")
window.configure(padx=100, pady=10, fg_color=LIGHT_BEIGE)

# Title Label styling
title_label = ctk.CTkLabel(window, text="Timer", text_color=DARK_BROWN, bg_color=LIGHT_BEIGE, font=(FONT_NAME, 50, "bold"))
title_label.pack(pady=(20, 10))

# Load and resize the image
image = Image.open("IMG_0670.PNG")  # Path to your image
image = image.resize((200, 224), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Canvas styling for the image
canvas = ctk.CTkCanvas(window, width=200, height=224, bg=LIGHT_BEIGE, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
canvas.pack(pady=10)

# Timer text label styling under the canvas
timer_label = ctk.CTkLabel(window, text="00:00", text_color=LIGHT_YELLOW, bg_color=LIGHT_BEIGE, font=(FONT_NAME, 35, "bold"))
timer_label.pack(pady=10)

# Start button styling
start_button = ctk.CTkButton(
    window,
    text="Start",
    fg_color=YELLOW_BEIGE,
    bg_color=LIGHT_BEIGE,
    border_color=LIGHT_BEIGE,
    text_color=DARK_BROWN,
    hover_color=GOLDEN_BROWN,  # Color change on hover
    font=(FONT_NAME, 12, "bold"),
    command=start_timer,
    corner_radius=20
)
start_button.pack(side="left", padx=20, pady=20, expand=True)

# Reset button styling
reset_button = ctk.CTkButton(
    window,
    text="Reset",
    fg_color=GOLDEN_BROWN,
    bg_color=LIGHT_BEIGE,
    border_color=LIGHT_BEIGE,
    text_color=LIGHT_YELLOW,
    hover_color="#DFC57B",  # Color change on hover
    font=(FONT_NAME, 12, "bold"),
    command=reset_timer,
    corner_radius=20
)
reset_button.pack(side="right", padx=20, pady=20, expand=True)

# Checkmarks label styling
check_marks = ctk.CTkLabel(window, text="", text_color=DARK_BROWN, bg_color=LIGHT_BEIGE, font=(FONT_NAME, 15, "bold"))
check_marks.pack(pady=10)

window.mainloop()

