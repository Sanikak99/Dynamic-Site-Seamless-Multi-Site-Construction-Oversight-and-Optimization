from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import Canvas, Text, Scrollbar, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\assets\frame0")

def open_excel_sheet(excel_file_path):
    os.startfile(excel_file_path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_excel_on_canvas(canvas, excel_file_path):

    canvas.delete("excel_text")
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Create a Text widget to display the Excel sheet
    text_widget = Text(canvas, wrap="none", name="excel_text")
    text_widget.pack(expand=True, fill="both")

    # Display the DataFrame in the Text widget
    text_widget.insert("end", df.to_string(index=False))

window = tk.Tk()
window.geometry("1637x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=1637,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:(display_excel_on_canvas(canvas, r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\SU_RTBI.xlsx")),
    relief="flat"
)
button_1.place(x=28.0, y=50.0, width=337.1099853515625, height=329.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:(display_excel_on_canvas(canvas, r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\D_RTBI.xlsx")),
    relief="flat"
)
button_2.place(x=28.0, y=421.0, width=337.1058044433594, height=329.0)


button_4 = tk.Button(
    text="Edit Sheet D",
    font=("Helvetica", 25),  # Adjust font size
    bg="#E0B0FF",  # Change background color to green
    fg="black",  # Change text color to white
    borderwidth=2,  # Add border width for 3D effect
    relief="raised",  # Use "raised" relief for 3D effect
    command=lambda:open_excel_sheet(r"C:\Users\Sanika\Documents\Project II\build_W_RTBI\D_RTBI.xlsx")
)
button_4.place(x=845.0, y=650.0, width=250, height=90)
canvas.place(x=432, y=45,width=1055, height=600)

window.resizable(True, True)
window.mainloop()

