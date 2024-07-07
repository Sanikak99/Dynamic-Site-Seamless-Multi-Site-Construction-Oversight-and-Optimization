from pathlib import Path
from subprocess import run
from tkinter import Toplevel, Label, Button
from tkinter import simpledialog
import threading

def run_in_thread(command):
    thread = threading.Thread(target=run, args=(command,))
    thread.start()

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanika\Documents\Project II\build_login\assets\frame0")

def open_gui():
    run(["python",str(Path(r"C:\Users\Sanika\Documents\Project II\build site selection\gui.py"))])
def open_gui1RTBIS():
    run(["python",str(Path(r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\gui - Copy (2).py"))])
def open_gui2RTBID():
    run(["python",str(Path(r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\gui - Copy.py"))])
def open_gui3SAS():
    run(["python",str(Path(r"C:\Users\Sanika\Documents\Project II\build_W_SA\gui - Copy.py"))])
def open_gui4SAW():
    run(["python",str(Path(r"C:\Users\Sanika\Documents\Project II\build_W_SA\gui - Copy - Copy.py"))])

def check_password(entry_widget):

    correct_password = "12345"

    entered_password = entry_widget.get()

    if entered_password == correct_password:
        open_gui()
    else:
        print("Incorrect password. Try again.")

def check_desigation(entry_widget2,entry_widget1):

    correct_password1 = "12345"
    correct_password2 = "54321"
    correct_password3 = "13579"
    correct_desigation1 = "CEO"
    correct_desigation2 = "Supervisor RTBI"
    correct_desigation3 = "Driver RTBI"
    correct_desigation4 = "Supervisor SA"
    correct_desigation5 = "Worker SA"

    entered_password = entry_widget2.get()
    entered_desigation = entry_widget1.get()

    if entered_desigation == correct_desigation1 and entered_password == correct_password1:
        open_gui()
    if entered_desigation == correct_desigation2 and entered_password == correct_password2:
        open_gui1RTBIS()
    if entered_desigation == correct_desigation3 and entered_password == correct_password3:
        open_gui2RTBID()
    if entered_desigation == correct_desigation4 and entered_password == correct_password2:
        open_gui3SAS()
    if entered_desigation == correct_desigation5 and entered_password == correct_password3:
        open_gui4SAW()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1637x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1637,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1336.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    301.0,
    400.00001110709854,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    343.0,
    170.37664794921875,
    image=image_image_3
)

canvas.create_text(
    965.0,
    178.0,
    anchor="nw",
    text="LOGIN ",
    fill="#000000",
    font=("K2D Regular", 96 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_desigation(entry_2,entry_1) ,
    relief="flat"
)
button_1.place(
    x=929.8550415039062,
    y=676.8751220703125,
    width=246.99293518066406,
    height=65.9906997680664
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1053.0,
    468.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFA263",
    fg="#000716",
    highlightthickness=0,
    font= 28
)
entry_1.place(
    x=771.0,
    y=441.0,
    width=564.0,
    height=53.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1053.0,
    558.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFA263",
    fg="#000716",
    highlightthickness=0,
    show='*',
    font= 30
)
entry_2.place(
    x=771.0,
    y=531.0,
    width=564.0,
    height=53.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    633.0,
    471.0,
    image=image_image_4
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1053.0,
    379.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFA263",
    fg="#000716",
    highlightthickness=0,
    font= 30
)
entry_3.place(
    x=771.0,
    y=352.0,
    width=564.0,
    height=53.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    686.0,
    385.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    658.0,
    557.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    900.0,
    209.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    974.0,
    207.0,
    image=image_image_8
)
window.resizable(True, True)
window.mainloop()
