from subprocess import run
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\\Sanika\\Documents\\Project II\\build site selection\\assets\\frame0")

def run_in_thread(command):
    thread = threading.Thread(target=run, args=(command,))
    thread.start()

def open_gui2():
    run_in_thread(["python", str(Path(r"C:\\Users\\Sanika\\Documents\\Project II\\build airport\\gui.py"))])

def open_gui3():
    run_in_thread(["python", str(Path(r"C:\\Users\\Sanika\\Documents\\Project II\\build_Sangli\\gui.py"))])

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
    818.0,
    104.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    486.0,
    123.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui3,
    relief="flat"
)
button_1.place(
    x=45.5234375,
    y=529.0,
    width=1460.510986328125,
    height=258.0000305175781
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
    relief="flat"
)
button_2.place(
    x=45.113037109375,
    y=239.04150390625,
    width=1463.92138671875,
    height=276.57916259765625
)

window.resizable(True, True)
window.mainloop()

